from typing import Any, Callable, Optional
from tornado.web import RequestHandler


class BaseMiddleware:
    """中间件基类"""

    def __init__(self, handler: RequestHandler) -> None:
        self.handler = handler

    async def process_request(self) -> Optional[Any]:
        """请求处理前的钩子"""
        pass

    async def process_response(self) -> Optional[Any]:
        """响应处理前的钩子"""
        pass


class MiddlewareManager:
    """中间件管理器，用于注册和执行中间件"""

    _middleware_classes = []

    @classmethod
    def register(cls, middleware_class: type) -> None:
        """注册中间件类"""
        if middleware_class not in cls._middleware_classes:
            cls._middleware_classes.append(middleware_class)

    @classmethod
    def get_middleware_instances(cls, handler: RequestHandler) -> list:
        """获取所有中间件实例"""
        return [middleware_class(handler) for middleware_class in cls._middleware_classes]

    @classmethod
    def apply_middleware(cls, method: Callable) -> Callable:
        """应用中间件装饰器"""
        async def wrapper(handler: RequestHandler, *args: Any, **kwargs: Any) -> Any:
            # 执行请求中间件
            for middleware in cls.get_middleware_instances(handler):
                result = await middleware.process_request()
                if result is not None:
                    return result

            # 执行原始请求
            result = await method(handler, *args, **kwargs)

            # 执行响应中间件
            for middleware in cls.get_middleware_instances(handler):
                response = await middleware.process_response()
                if response is not None:
                    return response

            return result
        return wrapper
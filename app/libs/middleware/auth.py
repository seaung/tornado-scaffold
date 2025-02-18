from typing import Optional, Any
from tornado.web import RequestHandler
from app.libs.middleware import BaseMiddleware
from app.libs.utils.response import ResponseWrapper


class TokenAuthMiddleware(BaseMiddleware):
    """Token验证中间件"""

    def __init__(self, handler: RequestHandler) -> None:
        super().__init__(handler)
        self.white_list = [
            '/api/v1/user/login/',
            '/api/v1/user/register/'
        ]

    async def process_request(self) -> Optional[Any]:
        """验证请求中的token"""
        # 白名单路径不需要验证token
        if self.handler.request.path in self.white_list:
            return None

        # 获取请求头中的token
        token = self.handler.request.headers.get('Authorization')
        if not token:
            return self.handler.finish(ResponseWrapper.error(
                code=401,
                message='未提供认证token'
            ))

        # 验证token格式
        try:
            token_type, token_value = token.split(' ')
            if token_type.lower() != 'bearer':
                return self.handler.finish(ResponseWrapper.error(
                    code=401,
                    message='无效的token格式'
                ))
        except ValueError:
            return self.handler.finish(ResponseWrapper.error(
                code=401,
                message='无效的token格式'
            ))

        # TODO: 在这里添加token的具体验证逻辑
        # 例如：验证token是否过期，是否被篡改等
        # 如果验证失败，返回相应的错误响应

        return None
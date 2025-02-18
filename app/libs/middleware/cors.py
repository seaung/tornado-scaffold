from typing import Optional, Any
from tornado.web import RequestHandler
from app.libs.middleware import BaseMiddleware


class CORSMiddleware(BaseMiddleware):
    """处理跨域请求的中间件"""

    def __init__(self, handler: RequestHandler) -> None:
        super().__init__(handler)
        self.allow_origin = '*'
        self.allow_methods = 'GET, POST, PUT, DELETE, OPTIONS'
        self.allow_headers = 'Content-Type, Authorization, X-Requested-With'
        self.allow_credentials = True

    async def process_request(self) -> Optional[Any]:
        """处理OPTIONS预检请求"""
        if self.handler.request.method == 'OPTIONS':
            self.handler.set_status(204)
            self.handler.finish()
            return True

    async def process_response(self) -> Optional[Any]:
        """为响应添加CORS相关的头部"""
        self.handler.set_header('Access-Control-Allow-Origin', self.allow_origin)
        self.handler.set_header('Access-Control-Allow-Methods', self.allow_methods)
        self.handler.set_header('Access-Control-Allow-Headers', self.allow_headers)
        if self.allow_credentials:
            self.handler.set_header('Access-Control-Allow-Credentials', 'true')
        return None
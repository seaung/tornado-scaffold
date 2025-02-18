from tornado.web import RequestHandler
from app.libs.utils.response import ResponseWrapper


class UserRequestHandler(RequestHandler):
    @MiddlewareManager.apply_middleware
    async def get(self):
        return self.finish(ResponseWrapper.success(data={'msg': 'ok'}))

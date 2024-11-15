from tornado.web import RequestHandler


class UserRequestHandler(RequestHandler):
    def get(self):
        return self.finish({'msg': 'ok'})

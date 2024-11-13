import tornado

from app import create_app


if __name__ == '__main__':
    app = create_app()
    app.listen(9527)
    tornado.ioloop.IOLoop().current().start()

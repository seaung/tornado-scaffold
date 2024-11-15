import tornado

from app import create_app


if __name__ == '__main__':
    try:
        print('[+] starting the web server on : 9527')
        app = create_app()
        app.listen(9527)
        tornado.ioloop.IOLoop().current().start()
    except KeyboardInterrupt:
        print('[-] shutdown the web promming...')

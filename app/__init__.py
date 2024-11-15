from tornado.web import Application


def create_app() -> Application:
    from app.api import urlpatterns

    app = Application(handlers=urlpatterns)

    return app

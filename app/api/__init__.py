from app.api.v1 import UserRequestHandler


urlpatterns = [
    (r'/api/v1/user/get/', UserRequestHandler),
]

import jwt
import datetime

from app.configs.settings import config


def generate_jwt(payload, exp_minutes=60):
    payload['exp'] = datetime.datetime.utcnow(
    ) + datetime.timedelta(minutes=exp_minutes)
    token = jwt.encode(payload, config.JWT_SECRET, algorithm='HS256')
    return token

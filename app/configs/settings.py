import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Config:
    DEBUG = True

    PORT = 9527

    JWT_SECRET = 'jwt_secret'

    DATABASE_URI = ''


config = Config()

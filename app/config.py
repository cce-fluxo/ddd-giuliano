from .sensive import Sensive as sensive


class Config:
    DEBUG = sensive.DEBUG
    SQLALCHEMY_DATABASE_URI = sensive.SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = sensive.SQLALCHEMY_TRACK_MODIFICATIONS
    JSON_SORT_KEYS = sensive.JSON_SORT_KEYS

    JWT_SECRET_KEY = sensive.JWT_SECRET_KEY

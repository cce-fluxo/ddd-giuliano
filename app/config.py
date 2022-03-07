from os import environ, path, pardir
from dotenv import load_dotenv

env_path = path.abspath(path.join(path.dirname(__file__), pardir))
load_dotenv(path.join(env_path, 'env.env'))


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://nzzyprruvvexht:0d1d2faf66822b24e7f6b4efb4b7db83eafc59275e625ee52d9a5e61ce40a476@ec2-54-158-26-89.compute-1.amazonaws.com:5432/d5qts8p9u1iust'
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    JSON_SORT_KEYS = environ.get('JSON_SORT_KEYS')

    #JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')
    JWT_SECRET_KEY = 'DKJNBASIJLDHUHubsuiaduiiuBUIYFGSAYG7WAUDH7328432978dajsbdhkuasgyuYDSABDKSAHJHU09E782916'

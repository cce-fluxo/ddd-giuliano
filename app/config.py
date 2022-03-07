from os import environ, path, pardir
from dotenv import load_dotenv

env_path = path.abspath(path.join(path.dirname(__file__), pardir))
load_dotenv(path.join(env_path, 'env.env'))


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://asxcpewbleavhb:1cc88c333ad9e6d4c3407716350f6c6721f27872047957fbc962f6be68f0fa97@ec2-34-231-183-74.compute-1.amazonaws.com:5432/dcb8acgifegipn'
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    JSON_SORT_KEYS = environ.get('JSON_SORT_KEYS')

    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')

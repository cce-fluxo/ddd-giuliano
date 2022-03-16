from os import environ, path, pardir
from dotenv import load_dotenv

env_path = path.abspath(path.join(path.dirname(__file__), pardir))
load_dotenv(path.join(env_path, 'env.env'))


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://kkjwdrngewrutr:7428d096f0c7f5e874fb0162b80a14e9260b1e793199a8bcd935c1e183aafaf8@ec2-54-158-26-89.compute-1.amazonaws.com:5432/d34beun2ckt3s'
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    JSON_SORT_KEYS = environ.get('JSON_SORT_KEYS')

    #JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')
    JWT_SECRET_KEY = 'DKJNBASIJLDHUHubsuiaduiiuBUIYFGSAYG7WAUDH7328432978dajsbdhkuasgyuYDSABDKSAHJHU09E782916'

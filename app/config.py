from os import environ, path, pardir
from dotenv import load_dotenv

env_path = path.abspath(path.join(path.dirname(__file__), pardir))
load_dotenv(path.join(env_path, 'env.env'))


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://nqhqyntcxhxbij:3f94c78b2180a9c6a5f8a0ab4a48e09544901f5d2223c8338ac04e06131ec589@ec2-18-210-191-5.compute-1.amazonaws.com:5432/d83nl2e1n9n45u'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False

    #JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')
    JWT_SECRET_KEY = 'DKJNBASIJLDHUHubsuiaduiiuBUIYFGSAYG7WAUDH7328432978dajsbdhkuasgyuYDSABDKSAHJHU09E782916'
    
    ## MAIL ## 
    MAIL_SERVER = environ.get('MAIL_SERVER')
    MAIL_PORT = environ.get('MAIL_PORT')
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_USE_TLS = True
    MAIL_USE_SSH = False
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')

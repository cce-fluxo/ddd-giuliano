from os import environ, path, pardir
from dotenv import load_dotenv

env_path = path.abspath(path.join(path.dirname(__file__), pardir))
load_dotenv(path.join(env_path, 'env.env'))


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://gktohrbnaxeuxh:158da6b202e7d64eac0f9382fc828dfa73dec7a6e5943f700281aec2d3ed70b6@ec2-3-230-238-86.compute-1.amazonaws.com:5432/d4sksot361k9qd'
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    JSON_SORT_KEYS = environ.get('JSON_SORT_KEYS')

    #JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')
    JWT_SECRET_KEY = 'DKJNBASIJLDHUHubsuiaduiiuBUIYFGSAYG7WAUDH7328432978dajsbdhkuasgyuYDSABDKSAHJHU09E782916'

import os

class Config(object):
    SECRET_KYE = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
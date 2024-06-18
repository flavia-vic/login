import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://pi:raspberry@192.168.1.10/login'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

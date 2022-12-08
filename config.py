import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__name__))

load_dotenv(os.path.join(basedir, '.env'))

class Config():
    SECRET_KEY=os.environ.get('SECRET_KEY')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    FLASK_APP=os.environ.get('FLASK_APP')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS= False
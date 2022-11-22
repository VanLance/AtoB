import os

class Config():
    SECRET_KEY=os.environ.get('SECRET_KEY')
    FLASK_APP=os.environ.get('FLASK_APP')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS= False
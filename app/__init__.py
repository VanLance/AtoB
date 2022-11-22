from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from config import Config
from flask_login import LoginManager


login = LoginManager()

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy()
migrate = Migrate(compare_type=True)

db.init_app(app)
migrate.init_app(app,db)
login.init_app(app)

login.login_view = 'login'
login.login_message = 'Please make sure you are logged in!'
login.login_message_category = 'warning'

from .auth.routes import auth as auth_bp
app.register_blueprint(auth_bp)

from app import routes,models
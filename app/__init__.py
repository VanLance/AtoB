from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from config import Config
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager()
db = SQLAlchemy()
migrate = Migrate(compare_type=True)

db.init_app(app)
migrate.init_app(app,db)
login.init_app(app)

login.login_view = 'login'
login.login_message = 'Please make sure you are logged in!'
login.login_message_category = 'warning'

from app.blueprints.auth.routes import auth as auth_bp
from app.blueprints.service.routes import service_bp
from app.blueprints.main import main as main_bp

app.register_blueprint(auth_bp)
app.register_blueprint(service_bp)
app.register_blueprint(main_bp)

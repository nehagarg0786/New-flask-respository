from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config
from flask_login import LoginManager, login_user, UserMixin, logout_user, login_required


app = Flask(__name__)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view="login"



from app import views, models
from app import admin_views


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.pagedown import PageDown
from config import config

db = SQLAlchemy()
bootstrap = Bootstrap()
moment = Moment()
pagedown = PageDown()
login_manager = LoginManager()
login_manager.login_view = 'admin.login'
login_manager.session_protection = 'strong'

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	db.init_app(app)
	bootstrap.init_app(app)
	moment.init_app(app)
	login_manager.init_app(app)
	pagedown.init_app(app)

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	from .admin import admin as admin_blueprint
	app.register_blueprint (admin_blueprint,url_prefix='/admin')

	return app


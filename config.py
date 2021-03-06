import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	FLASK_POSTS_PER_PAGE = 10

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = \
			'sqlite:///' + os.path.join(basedir,'data-dev.sqlite')

class TestingConfig(Config):
	TESTING = True
	WTF_CSRF_ENABLED = False
	SQLALCHEMY_DATABASE_URI = \
			'sqlite:///' + os.path.join(basedir,'data-test.sqlite')

class ProductionCofig(Config):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = \
			'sqlite:///' + os.path.join(basedir,'data.sqlite')

config = {
	'development':DevelopmentConfig,
	'testing':TestingConfig,
	'production':ProductionCofig,

	'default':DevelopmentConfig
}
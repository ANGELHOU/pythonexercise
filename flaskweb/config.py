import os
class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True

	@staticmethod
	def init_app(app):
		pass	

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/test'

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/test'

config = {
	'development' : DevelopmentConfig,
	'testing' : TestingConfig,
	'default' : TestingConfig
}

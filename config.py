import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default_secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('mysql+pymysql://root:Root*2024@196.41.38.46:60091/leave_management')

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('mysql+pymysql://root:Root*2024@196.41.38.46:60091/leave_management')
    DEBUG = True

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('mysql+pymysql://root:rRoot*2024@196.41.38.46:60091/tutorial_database')
    TESTING = True

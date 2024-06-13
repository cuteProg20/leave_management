import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:rRoot*2024@196.41.38.46:60091/tutorial_database')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# class TestingConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get('mysql+pymysql://root:rRoot*2024@196.41.38.46:60091/tutorial_database')
#     TESTING = True
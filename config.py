import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:Root*2024@196.41.38.46:60091/leave_management')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
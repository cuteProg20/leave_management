from flask import Flask
from flask import render_template
from config import TestingConfig
from .Models import db 
from flask_migrate import Migrate
import os
# 
# from flask_sqlalchemy import SQLAlchemy
# 

app= Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', TestingConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize the database and migration
db.init_app(app)
migrate = Migrate(app, db)

@app.before_first_request
def create_tables():
    db.create_all()




@app.route('/')
def home():
    return render_template('/home.html')


if __name__ == '__main__':
    app.run(debug=True)
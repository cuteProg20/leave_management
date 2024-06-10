from flask import Flask, render_template
from flask_migrate import Migrate
from config import TestingConfig
# from app import app
import os
from .Models.users import db

app= Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', TestingConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize the database and migration
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def create_tables():
    db.create_all()

@app.route('/home')   
def home():
    return render_template('/home.html')


if __name__ == '__main__':
    app.run(debug=True)
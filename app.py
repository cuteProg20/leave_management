from flask import Flask, render_template
from flask_migrate import Migrate
from apps import db, create_app
import os


app= Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def create_tables():
    db.create_all()

# @app.route('/home')   
# def home():
#     return render_template('apps/Templates/home.html')


if __name__ == '__main__':
    app.run(debug=True)
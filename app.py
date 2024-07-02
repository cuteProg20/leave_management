from flask import Flask, render_template
from flask_migrate import Migrate
from apps import db, create_app
import os

<<<<<<< HEAD
=======
app = create_app()
migrate = Migrate(app, db)
>>>>>>> 6be26e20d84ce904fc952c8113db523893adaad1

app= Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def create_tables():
    db.create_all()

<<<<<<< HEAD
# @app.route('/home')   
# def home():
#     return render_template('apps/Templates/home.html')
=======
@app.route('/home')   
def home():
    return render_template('apps/Templates/home.html')
>>>>>>> 6be26e20d84ce904fc952c8113db523893adaad1


if __name__ == '__main__':
    app.run(debug=True)
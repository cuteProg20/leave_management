from flask import Flask
from flask import render_template
from .Models import db
# from flask_migrate import migrate
# from flask_sqlalchemy import SQLAlchemy
# import os

app= Flask(__name__)
@app.route('/')
def home():
    return render_template('/home.html')

if __name__ == '__main__':
    app.run(debug=True)
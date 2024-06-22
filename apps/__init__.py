from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS

# Extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    CORS(app)

    # Register blueprints
    from .auth import auth_bp
    from leaves import leave_bp
    from .leave_requests import leave_request_bd
    from .employee import employee_bp
    from .departments import department_bp
    from .country import country_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(leave_bp, url_prefix='/api/leave')
    app.register_blueprint(employee_bp, url_prefix='/api/employee')
    app.register_blueprint(department_bp, url_prefix='/api/department')
    app.register_blueprint(country_bp, url_prefix='/api/country')
    app.register_blueprint(leave_request_bd, url_prefix='/api/leave_request')

    return app
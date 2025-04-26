# app/__init__.py

from flask import Flask
from flask_mysqldb import MySQL
from flask_session import Session
from flask_cors import CORS

mysql = MySQL()

def create_app():
    app = Flask(__name__)

    # Basic Configuration
    app.config['SECRET_KEY'] = 'your-secret-key'   # Change this in production!
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'your_mysql_username'
    app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
    app.config['MYSQL_DB'] = 'enhanced_auth_system'
    app.config['SESSION_TYPE'] = 'filesystem'  # Using filesystem sessions

    # Initialize Extensions
    mysql.init_app(app)
    Session(app)
    CORS(app)  # Enable Cross-Origin Resource Sharing if needed

    # Import and Register Blueprints
    from app.routes.auth import auth_bp
    from app.routes.admin import admin_bp
    from app.routes.user import user_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)

    return app

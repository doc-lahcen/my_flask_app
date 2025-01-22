from flask import Flask
import mysql.connector
from mysql.connector import Error

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['DEBUG'] = True  # Enable debug mode

    # Database configuration
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'fsts@2025'
    app.config['MYSQL_DATABASE'] = 'app_data'

    # Register Blueprints (controllers)
    from app.controllers.main_controller import main
    app.register_blueprint(main)

    return app

from flask import Blueprint, render_template, jsonify
import mysql.connector
from mysql.connector import Error

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/test_db')
def test_db():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='fsts@2025',
            database='app_data'
        )
        if connection.is_connected():
            return jsonify({"message": "Connected to the database!"})
    except Error as e:
        return jsonify({"error": str(e)})
    finally:
        if connection and connection.is_connected():
            connection.close()

@main.route('/presentation')
def presentation():
    return render_template('presentation.html')

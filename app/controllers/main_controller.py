from flask import Blueprint, render_template, jsonify, request
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
            host='192.168.1.111',
            user='root',
            password='fsts@2025',
            database='app_data',
            port=33006
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

@main.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        connection = None
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='fsts@2025',
                database='app_data',
                port=33006
            )
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (username, password, email))
            connection.commit()
            return jsonify({"message": "User added successfully!"})
        except Error as e:
            return jsonify({"error": str(e)})
        finally:
            if connection and connection.is_connected():
                connection.close()
    return render_template('add_user.html')

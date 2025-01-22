from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Enregistrer les Blueprints (contrôleurs)
    from app.controllers.main_controller import main
    app.register_blueprint(main)

    return app

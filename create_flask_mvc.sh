#!/bin/bash

# Nom du projet
PROJECT_NAME="my_flask_app"

# Création de la structure du projet
echo "Création de la structure du projet Flask MVC..."
mkdir -p $PROJECT_NAME/{app/{controllers,models,templates,static/{css,js}},}
touch $PROJECT_NAME/{run.py,requirements.txt}
touch $PROJECT_NAME/app/{__init__.py,controllers/__init__.py,models/__init__.py}

# Contenu du fichier __init__.py (initialisation Flask)
cat <<EOF > $PROJECT_NAME/app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Enregistrer les Blueprints (contrôleurs)
    from app.controllers.main_controller import main
    app.register_blueprint(main)

    return app
EOF

# Contenu du contrôleur principal
cat <<EOF > $PROJECT_NAME/app/controllers/main_controller.py
from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')
EOF

# Contenu du modèle User
cat <<EOF > $PROJECT_NAME/app/models/user_model.py
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<User {self.name}>"
EOF

# Contenu de la vue HTML
cat <<EOF > $PROJECT_NAME/app/templates/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <title>Accueil</title>
</head>
<body>
    <h1>Bienvenue sur l'application Flask MVC</h1>
</body>
</html>
EOF

# Fichier CSS de base
cat <<EOF > $PROJECT_NAME/app/static/css/style.css
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f9;
    color: #333;
    margin: 0;
    padding: 0;
    text-align: center;
}
EOF

# Point d'entrée de l'application
cat <<EOF > $PROJECT_NAME/run.py
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
EOF

# Fichier requirements.txt
cat <<EOF > $PROJECT_NAME/requirements.txt
flask
EOF

# Message de fin
echo "Structure du projet Flask MVC créée avec succès dans le dossier '$PROJECT_NAME'."
echo "N'oubliez pas d'exécuter la commande suivante pour installer les dépendances :"
echo "    pip install -r requirements.txt"
echo "Pour démarrer l'application :"
echo "    python run.py"

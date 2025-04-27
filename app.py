# On importe les modules nécessaires
from flask import Flask, render_template, request  # Flask pour l'application web
import os                                           # Pour gérer les fichiers
from werkzeug.utils import secure_filename          # Pour sécuriser le nom des fichiers uploadés
import random                                       # Pour simuler un résultat aléatoire

# On crée notre application Flask
app = Flask(__name__)

# On définit le dossier où les images uploadées seront stockées
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Route principale → Page d'accueil (formulaire d'upload)
@app.route('/')
def index():
    return render_template('index.html')  # On affiche le fichier HTML index.html

# Route qui gère l'envoi du fichier (image)
@app.route('/upload', methods=['POST'])  # On accepte uniquement la méthode POST
def upload():
    # Vérifie s’il y a bien un fichier image dans la requête
    if 'image' not in request.files:
        return "Aucune image reçue", 400  # Code 400 = erreur

    file = request.files['image']  # Récupère le fichier
    if file.filename == '':
        return "Nom de fichier vide", 400  # Vérifie qu’un fichier a été sélectionné

    # On sécurise le nom du fichier (enlève les caractères spéciaux)
    filename = secure_filename(file.filename)

    # On crée le chemin complet où l’image sera enregistrée
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # On enregistre le fichier image dans le dossier 'uploads'
    file.save(file_path)

    # === 🔬 Simulation d’un diagnostic avec IA (aléatoire pour l’instant) ===
    maladies = [
        "Pneumonie détectée",
        "Aucune anomalie",
        "Opacité suspecte",
        "Infection probable"
    ]
    resultat = random.choice(maladies)  # Choisit un diagnostic au hasard
    probabilite = round(random.uniform(70, 99), 2)  # Un pourcentage entre 70% et 99%

    # On renvoie la page HTML resultat.html avec les informations
    return render_template(
        "resultat.html",
        image_path=file_path,         # Le chemin de l’image à afficher
        resultat=resultat,            # Le diagnostic simulé
        probabilite=probabilite       # Le pourcentage simulé
    )

# Pour lancer l'application Flask localement (on exécute ça uniquement si ce fichier est exécuté directement)
if __name__ == '__main__':
    app.run(debug=True)






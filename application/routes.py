from flask import Flask, render_template, request
from sqlalchemy import null
from datetime import datetime

app = Flask(__name__)


# Montrer à flask là où se trouve notre fichier de config
app.config.from_object("config")

from .models import (Reservation,saveReservation)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    message = ""  # Initialiser le message à une chaîne vide
    if request.method == 'POST':
        tel= request.form['tel']
        dateA= request.form['dateA']
        dateD= request.form['dateD']
        dateAr=datetime.strptime(dateA,'%Y-%m-%d').date()
        dateDe=datetime.strptime(dateD, '%Y-%m-%d').date()
        nbresPersonnes= request.form['nbrePersonnes']
        nbresChambres= request.form['nbreChambres']
        nomC= request.form['nom']
        # Créer un objet de type Réservation
        new_reservation=Reservation(dateArrivee=dateAr, dateDepart=dateDe, nombrePersonnes=nbresPersonnes, nbreChambres=nbresChambres, nomClient=nomC, telClient=tel)
        if new_reservation != null:
            # insérer cet objet dans la bd
            saveReservation(new_reservation) 
            message = "Votre réservation a été enregistrée avec succès !"
    
    return render_template('home.html',msg=message)


@app.route("/gallery")
def page():
    return render_template('gallery.html')

@app.route("/about")
def about_us():
    return render_template('about_us.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/témoignages")
def page_temoignages():
    return render_template('temoignages.html')

#réservation
@app.route("/réservation")
def page_reservation():
    return render_template('ges_area/views/reservation.html')

#connexion
@app.route("/connexion")
def connexion():
    return render_template('connexion.html')


# les entités #from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from .routes import app
from flask import redirect,url_for,render_template
from flask_bcrypt import Bcrypt



# # Créer une instance de la base de donnees
# db = SQLAlchemy()
# # Relier la base de donnee avec l'application
# db.init_app(app)
# OU BIEN
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)




# Définir la classe Reservation
class Reservation(db.Model):
    __tablename__ = 'reservations'
    id=db.Column(db.Integer, primary_key=True)
    dateArrivee=db.Column(db.Date)
    dateDepart=db.Column(db.Date)
    nomClient=db.Column(db.String(200))
    nombrePersonnes=db.Column(db.Integer)
    telClient=db.Column(db.String(200))
    nbreChambres=db.Column(db.Integer)
 

# Définir la classe Message
class Message(db.Model):
    __tablename__ = 'message'
    id=db.Column(db.Integer, primary_key=True)
    nom=db.Column(db.String(150))
    email=db.Column(db.String(200))
    suject=db.Column(db.String(200))
    message=db.Column(db.String)
    
# Définir la classe Avis
class Avis(db.Model):
    __tablename__ = 'avis'
    id=db.Column(db.Integer, primary_key=True)
    nom=db.Column(db.String(150))
    note=db.Column(db.Double)
    message=db.Column(db.String)

# Définir la classe User:
class User(db.Model):
    __tablename__ = 'users'
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(150),unique=True)
    password=db.Column(db.String(150))
    
    def __init__(self, email, password):
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

##########
# Définir la fonction pour ajouter une réservation

def saveReservation(reservation: Reservation):
    db.session.add(reservation)
    db.session.commit()

# Définir la fonction pour récupérer les réservations
def get_reservations():
    reservations = []
    docs = db.collection('reservations').get()
    for doc in docs:
        data = doc.to_dict()
        reservation = Reservation(data['arrival_date'], data['departure_date'], data['person_type'], data['num_persons'], data['phone_number'])
        reservations.append(reservation)
    return reservations

""" 
# Définir les routes Flask
@app.route('/make_reservation', methods=['POST'])
def make_reservation():
    # Récupérer les données du formulaire
    arrival_date = request.form['arrival_date']
    departure_date = request.form['departure_date']
    person_type = request.form['person_type']
    num_persons = int(request.form['num_persons'])
    phone_number = request.form['phone_number']

    # Ajouter la réservation à Firestore
    add_reservation(arrival_date, departure_date, person_type, num_persons, phone_number)
    return redirect(url_for('index'))

    """
    
# Création des tables dans la base de données
#with app.app_context():
#db.session.commit()
#db.create_all() #créer toutes les tables dans la bd
# User.__table__.drop(db.engine) # supprimer une table spécifique
# db.drop_all(). # supprimer toutes les tables dans la bd

# Enregistrez les modifications dans la base de données
# db.session.commit()
# #
#
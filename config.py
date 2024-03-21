import os
import secrets

APP_NAME = "Hotel-Woezon"

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "db.sqlite")

# Générer une clé secrète sécurisée
SECRET_KEY = secrets.token_hex(16)

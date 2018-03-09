import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Initialize application
app = Flask(__name__, static_folder=None)

# app configuration
app_settings = os.getenv(
    'APP_SETTINGS',
    'app.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

# Initialize Bcrypt
bcrypt = Bcrypt(app)

# Initialize Flask Sql Alchemy
db = SQLAlchemy(app)

# Import the application views
from app import views

# Register blue prints
from app.auth.views import auth

app.register_blueprint(auth, url_prefix='/v1')

from app.canhap.views import conhap

app.register_blueprint(conhap, url_prefix='/v1')

from app.conhapitems.views import conhapitems

app.register_blueprint(conhapitems, url_prefix='/v1')

from app.docs.views import docs

app.register_blueprint(docs)

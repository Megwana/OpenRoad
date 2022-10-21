from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = "helloworld"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///openroad"
db = SQLAlchemy(app)

from .views import views
from .auth import auth

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')
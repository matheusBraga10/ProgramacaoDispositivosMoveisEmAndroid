from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import jose
import dynaconf
import datetime

app = Flask(__name__)
db = SQLAlchemy(app)
settings = FlaskDynaconf(
  app,
  settings_files=["settings.toml", ".secrets.toml"],
)

app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.MODIFICATIONS
app.config['SECRET_KEY'] = settings.SECRET_KEY
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import spacy

from .config import Config

db = SQLAlchemy()
nlp = spacy.load('en_core_web_lg')


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    return app

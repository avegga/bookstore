from dataclasses import dataclass
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)

@dataclass
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description  = db.Column(db.String)
    publish_year = db.Column(db.Integer)
    pages_count = db.Column(db.Integer)
    created_at = db.Column(db.String)




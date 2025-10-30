from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import JSON

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    roll_number = db.Column(db.String(20), unique=True, nullable=False)
    grades = db.Column(JSON, default={})

    def _repr_(self):
        return f'<Student {self.name}>'
from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    notes = db.relationship('Notes', backref='author', lazy=True) # Notes is reference to the class

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}' )"

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(350), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # user.id is reference to the table and column name

    def __repr__(self):
        return f"Note('{self.id}', '{self.content}', '{self.date_created}')"
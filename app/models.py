from datetime import datetime
from app import db

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(350), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Note('{self.id}', '{self.content}', '{self.date_created}')"
from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import Config
from forms import NoteForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'remember-to-chage-this-part-concha'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(350), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Note('{self.id}', '{self.content}', '{self.date_created}')"

@app.route("/")
@app.route("/index", methods=['GET', 'POST'])
def index():
    form = NoteForm()
    if form.validate_on_submit():
        content = Notes(content=form.content.data)
        db.session.add(content)
        db.session.commit()
        flash('Your note was created', 'success')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)







if __name__ == "__main__":
    app.run(debug=True)
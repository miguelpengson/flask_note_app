from flask import render_template, url_for, request, redirect, flash
from app import app, db
from app.forms import NoteForm
from app.models import Notes


@app.route("/")
@app.route("/index")
def index():
    notes = Notes.query.all()
    return render_template('index.html', notes=notes)


@app.route("/note/new", methods=['GET', 'POST'])    
def new_note():
    form = NoteForm()
    if form.validate_on_submit():
        note = Notes(title=form.title.data, content=form.content.data)
        db.session.add(note)
        db.session.commit()
        flash('Your note has been created!', 'success')
        return redirect(url_for('index'))
    return render_template('create_note.html', title='New Note', form=form, legend='New Note')


@app.route("/note/<note_id>")
def note(note_id):
    note = Notes.query.get_or_404(note_id)
    return render_template('note.html', title=note.title, note=note)
    
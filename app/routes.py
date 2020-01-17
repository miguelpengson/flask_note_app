from flask import render_template, url_for, request, redirect, flash
from app import app
from app.forms import NoteForm


@app.route("/")
@app.route("/index", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/note/new", methods=['GET', 'POST'])    
def new_note():
    form = NoteForm()
    if form.validate_on_submit():
        flash('Your note has been created!', 'success')
        return redirect(url_for('index'))
    return render_template('create_note.html', title='New Note', form=form, legend='New Note')
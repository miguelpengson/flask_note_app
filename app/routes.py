from flask import render_template, url_for, request, redirect, flash
from app import app, db, bcrypt
from app.forms import NoteForm, RegistrationForm, LoginForm
from app.models import Notes, User


@app.route("/")
@app.route("/index")
def index():
    notes = Notes.query.all()
    return render_template('index.html', notes=notes)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! Your can now log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@log.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful, Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

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
    
@app.route("/note/<note_id>/update", methods=['GET', 'POST'])
def update_note(note_id):
    note = Notes.query.get_or_404(note_id)
    form = NoteForm()
    if form.validate_on_submit():
        note.title = form.title.data
        note.content =  form.content.data
        db.session.commit()
        flash('Your note has been updated!', 'success')
        return redirect(url_for('index', note_id=note.id))
    elif request.method == 'GET':
        form.title.data = note.title
        form.content.data = note.content
    return render_template('create_note.html', title='Update Note', form=form,
                            legend='Update Note')

@app.route("/note/<note_id>/delete", methods=['POST'])
def delete_note(note_id):
    note = Notes.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    flash('Your note has been deleted!', 'success')
    return redirect(url_for('index'))
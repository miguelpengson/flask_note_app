from flask import Flask, render_template, url_for, request, redirect, flash
from app import app
from app.forms import NoteForm
from app.models import Notes




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
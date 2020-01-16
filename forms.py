from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, ValidationError

class NoteForm(FlaskForm):
    notes = TextAreaField('Notes', validators=[DataRequired()])
    submit = SubmitField('Add Notes')
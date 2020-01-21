from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=3, max=25)] )
    email = StringField('Email', validators=[DataRequired(), Email()] )                            
    password = PasswordField('Password', validators=[DataRequired()] )
    confirm_password = PasswordField('Confirm Password',
                                    validators=[DataRequired(), EqualTo('password')] )
    submit = SubmitField('Sign Up') 

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()] )                               
    password = PasswordField('Password', validators=[DataRequired()] )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class NoteForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Save')
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, MultipleFileField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=100)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember')
    submit = SubmitField('Login')


class ComplaintForm(FlaskForm):
    title = StringField('title',
                        validators=[DataRequired(), Length(min=2, max=20)])
    description = StringField('Username',
                              validators=[DataRequired(), Length(min=2, max=500)])
    location = StringField('location',
                           validators=[DataRequired(), Length(min=2, max=20)])
    media = MultipleFileField('Media')
    submit = SubmitField('Login')

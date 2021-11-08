import wtforms.widgets
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
    description = StringField('description',
                              validators=[DataRequired(), Length(min=2, max=500)],  widget=wtforms.widgets.TextArea())
    location = StringField('location',
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Login')

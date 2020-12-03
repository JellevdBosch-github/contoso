from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, PasswordField, BooleanField, SubmitField, ValidationError, \
    DateField, RadioField
from wtforms.validators import *


class RegistrationForm(FlaskForm):
    first_name = StringField('First name', validators=[InputRequired(), Length(3, 50)])
    middle_name = StringField('Middle name', validators=[Optional(), Length(2, 50)])
    last_name = StringField('Last name', validators=[InputRequired(), Length(3, 50)])
    emergency_name = StringField('Full emergency name', validators=[InputRequired(), Length(3, 150)])
    email = StringField('Email',
                        validators=[Email("Email validation error!"), InputRequired(), Length(6, 25)])
    password = PasswordField('Password', validators=[InputRequired(), Length(6, 50)])
    password_confirm = PasswordField('Repeat password', validators=[InputRequired(),
                                                                       EqualTo('password',
                                                                               message='Passwords must match!'),
                                                                       Length(6, 50)])
    gender = RadioField('Gender', choices=['m', 'f', 'o', 'u'], validators=[InputRequired()])
    title = StringField('Title', validators=[InputRequired(), Length(2, 8)])
    date_of_birth = DateField('Date of birth', format='%d-%m-%Y', validators=[InputRequired()])
    phone_number = StringField('Phone number', validators=[InputRequired(), Length(9, 25)])
    emergency_phone_number = StringField('Emergency Phone number', validators=[InputRequired(), Length(9, 25)])
    country = StringField('Country', validators=[InputRequired(), Length(4, 25)])
    city = StringField('City', validators=[InputRequired(), Length(3, 25)])
    postal_code = StringField('ZIP code', validators=[InputRequired(), Length(6, 6)])
    street = StringField('Street', validators=[InputRequired(), Length(3, 25)])
    house_number = StringField('House number', validators=[InputRequired(), Length(1, 5)])
    submit_register = SubmitField("Sign up")


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[Email("Email validation error!"), InputRequired(), Length(6, 25)])
    password = PasswordField('Password', validators=[InputRequired(), Length(6, 50)])
    submit_login = SubmitField("Sign up")


class ForgotPassword(FlaskForm):
    password = PasswordField('Password', validators=[InputRequired(), Length(6, 50)])
    password_confirm = PasswordField('Herhaal wachtwoord', validators=[InputRequired(),
                                                                       EqualTo('password',
                                                                               message='Passwords must match!'),
                                                                       Length(6, 50)])
    submit_reset = SubmitField("Reset")

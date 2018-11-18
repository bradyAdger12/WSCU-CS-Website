from package.database_model import User
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class FormCreateAccount(FlaskForm):
    firstname = StringField('First Name: ', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username: ', validators=[DataRequired(Length(min=5, max=20))])
    email = StringField('Email: ', validators=[DataRequired(Length(max=20)), Email()])
    password = PasswordField('Password: ', validators=[DataRequired(Length(min=8, max=25))])
    confirm_password = PasswordField('Confirm Password: ', validators=[DataRequired(Length(min=8, max=25)), EqualTo('password')])
    submit = SubmitField('Create Account')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken!')
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email is already taken!')


class FormLogin(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired(Length(min=8,max=25))])
    remember_me = BooleanField('Remember Me: ')
    submit = SubmitField('Login')


class FormUpdateAccount(FlaskForm):
    email = StringField('Update Email: ', validators=[DataRequired(Length(max=25)), Email()])
    username = StringField('Update Username: ', validators=[DataRequired(Length(min=8, max=25))])
    submit = SubmitField('Update Account')
    def validate_username(self, username):
        if current_user.username != username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username is already taken!')
    def validate_email(self, email):
        if current_user.email != email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email is already taken!')

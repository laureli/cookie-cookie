from flask.ext.wtf import Form, validators
from flask.ext.wtf import TextAreaField, FloatField, TextField, PasswordField, IntegerField, DateField, BooleanField, SelectField, RadioField, SelectMultipleField
import model

class LoginForm(Form):
    email = TextField('Email',
                      [validators.Email(message= (u'Invalid email address'))])
    password = PasswordField('Password', [validators.Required(), 
                             validators.length(min=6, max=25)])
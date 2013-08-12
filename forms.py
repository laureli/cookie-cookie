from flask.ext.wtf import Form, validators, Required, Length
from flask.ext.wtf import TextAreaField, TextField, PasswordField, IntegerField, BooleanField, SelectField, RadioField, SelectMultipleField
import model

class LoginForm(Form):
    email = TextField('Email', [validators.Email(message= (u'Invalid email address'))])
    username = TextField('Username', [validators.Email(message= (u'Invalid username address'))])
    password = PasswordField('Password', [validators.Required(), validators.length(min=6, max=25)])
    remember_me = BooleanField('remember_me', default = False)

class EditForm(Form):
	username = TextField('username', validator=[Required()])
	about_me = TextAreaField('about me', validators=[Length(min=0,max=140)])







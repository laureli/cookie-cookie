from flask.ext.wtf import Form, validators, Required, Length
from flask.ext.wtf import TextAreaField, TextField, SubmitField, PasswordField, IntegerField, BooleanField, SelectField, RadioField, SelectMultipleField
from model import *

class LoginForm(Form):
    email = TextField('Email', [validators.Email(message= (u'Invalid email address'))])
    password = PasswordField('Password', [validators.Required(), validators.length(min=6, max=25)])
    remember_me = BooleanField('remember_me', default = False)

class EditForm(Form):
	username = TextField('username', validator=[Required()])
	about_me = TextAreaField('about me', validators=[Length(min=0,max=140)])

class SignupForm(Form):
	username = TextField("First name",  [validators.Required("Please enter your first name.")])
	email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
	password = PasswordField('Password', [validators.Required("Please enter a password.")])
	submit = SubmitField("Create account")


	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)
 
	def validate(self):
		if not Form.validate(self):
			return False
     
		user = User.query.filter_by(email = self.email.data.lower()).first()
		if user:
			self.email.errors.append("That email is already taken")
			return False
		else:
			return True


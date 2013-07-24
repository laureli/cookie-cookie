from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/') # index!
def index():
	# splash page, organization + login
	return "cookie, hello, it is good to see you there, etc"

@app.route('/welcome.html') # splash page
def welcome():
	return "quoi!"
	#returning user welcome page

@app.route('/signup.html')
def sign_up():
	return "new user, put your information here"

@app.route('/')
def 




if __name__ == "__main__":
	app.run(debug=True)

from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/') # index!
def index():
	# splash page, organization 
	# send to _login_ if you are a returning user
	# send to _sign up_ for new users
	return "cookie, hello, it is good to see you there, etc"

@app.route('/login.html')
def login():
	return "hello, login here in html"

@app.route('/welcome.html') # splash page
def welcome():
	return "quoi, you return - we love you in html"
	#returning user welcome page

@app.route('/signup.html')
def sign_up():
	return "new user, put your information here in html"
	# new user sign up here

@app.route('/view_cookies')
def cookie_view():
	return "show me the cookies on your computer, returning user!"
	# existing user, see cookies there

@app.route('/show_cookies.html')
def show_cookies():
	return " here are some cookies, in html"


if __name__ == "__main__":
	app.run(debug=True)

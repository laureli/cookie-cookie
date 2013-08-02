from flask import Flask, render_template, request, redirect, jsonify

#configuration information
DATABASE = '/tmp/flaskr.db' 
DEBUG = True
SECRET_KEY = 'development key'
USERNAM = 'admin' 
PASSWORD = 'default'


#application
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('WEBL_SETTINGS', silent=True)

# what is up with multiline import statements?

@app.route('/view_cookies')
def cookie_view():
	return "show me the cookies on your computer, returning user!"
	# existing user, see cookies there

	domain = request.args.get('domain', 0, type=str)
	
	return jsonify(domain=a)


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    c = request.args.get('c', 0, type=int)
    return jsonify(result=a + b * c)


@app.route('/show_cookies.html')
def show_cookies():
	return "html showing cookies"


@app.route('/call_cookies.html')
def call_cookies():
	# return " here is where we designate domain to search, in html"
	return render_template("call_cookies.html")


@app.route('/') # index!
def index():
	# splash page, organization 
	# send to _login_ if you are a returning user
	# send to _sign up_ for new users
	return render_template('index.html')

# ################## practice for JSON
	

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






if __name__ == "__main__":
	app.run(debug=True)

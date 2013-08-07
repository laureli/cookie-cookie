from flask import Flask, render_template, request, redirect, jsonify
import schema
from schema import Cookie, User, session
import json

#configuration information
DATABASE = '/tmp/mixerapp.db' 
DEBUG = True
SECRET_KEY = 'development key'
USERNAM = 'admin' 
PASSWORD = 'default'


#application
app = Flask(__name__)
app.config.from_object(__name__)


# @app.route('/view_cookies', methods=['POST'], ['GET'])
# def cookie_view():
# 	return "show me the cookies on your computer, returning user!"
	# existing user, see cookies there



@app.route('/read_cookies', methods=['POST'])
def read_cookies():
	content = request.get_json()
		# content is a DICTIONARY!

	for c in content['cookies']:
		keys = c.keys()
		values = c.values()
		# keys and values are LISTS

		if values[0] == 'www.'+ request.form['requested_domain']+'.com':
			cookie_object = Cookie()
			cookie_object.set_cookie_from_browser(c)
		        session.add(cookie_object)
			session.commit()

	return jsonify(content)


@app.route('/set_browser_cookie', methods=['GET'])
def set_browser_cookie():

# REMEMBER: url and domain need to be THE SAME PLACE !!!

	return jsonify({"cookies": [
		{"url": "http://www.snazzy.com", 
		"name": "testCookie2", 
		"value": "sample-value-here2",
		"domain": "snazzy.com",}
		]
	})

@app.route('/call_cookies')
def call_cookies():
	# return " here is where we designate domain to search, in html"
	return render_template("call_cookies.html")


@app.route('/') # index!
def index():
	# splash page, organization 
	# send to _login_ if you are a returning user
	# send to _sign up_ for new users
	return render_template('index.html')



# ################## 
	

@app.route('/login')
def login():
	return "hello, login here in html"

@app.route('/welcome') # splash page
def welcome():
	return "quoi, you return - we love you in html"
	#returning user welcome page

@app.route('/signup')
def sign_up():
	return "new user, put your information here in html"
	# new user sign up here






@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    c = request.args.get('c', 0, type=int)
    return jsonify(result=a + b * c)


import os
from flask import send_from_directory

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
	app.run(debug=True)

import os
import json
from flask import Flask, render_template, send_from_directory, request, redirect, jsonify, g
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer

import model
from model import Cookie, User, session
from forms import LoginForm

# DB config information
DATABASE = '/tmp/mixerapp.db' 
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin' 
PASSWORD = 'default'


# application
app = Flask(__name__)
app.config.from_object(__name__)

### Start LoginHandler settings

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

@lm.user_loader
def load_user(id):
    return model.session.query(model.User).get(id)

@app.before_request
def before_request():
    g.user = current_user
    # this is used as 'current_user.id' or 'current_user.email'
   

### End LoginHandler settings

### start websocket settings

@app.route('/socket')
def socket():
	if request.environ.get('wsgi.websocket'):
		ws = request.environ['wsgi.websocket']
		while True:
			message = ws.receive()
			ws.send(message)
	return


@app.route('/test')
def test():
	return render_template('test.html')


### end websocket settings


### start login / logout

@app.route('/login', methods=["GET"])
def login():
    # if user hasn't logged out redirect don't reload login page
    if current_user is not None and current_user.is_authenticated():
        return redirect(url_for('user'))

    form = LoginForm()  
# LoginForm() is defined in the forms.py file
    if form.validate_on_submit():

        user= model.session.query(model.User).filter_by(email=form.email.data, password=form.password.data).first()
    
        if user is not None:
            login_user(user)
            flash("Welcome")
        else:
            flash("Invalid login")

        return redirect(request.args.get("next") or url_for('user'))
        
    
    return render_template('login.html',
                            title='Sign In',
                            form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
# REDIRECT BACK TO THE SPLASH PAGE
    return redirect('/index')

##### end login / logout



############### start managing users


@app.route('/') # index!
def index():
	# splash page for not-logged in users arriving not from extension
	# send to _login_ if you are a returning user
	# send to _sign up_ for new users
	return render_template('index.html')

# this does math on the index
@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    c = request.args.get('c', 0, type=int)
    return jsonify(result=a * b + c)


@app.route('/signup')
def sign_up():
	return "new user, put your information here in html"
	# new user sign up here


################ end managing users




################ start cookie management

@app.route('/read_cookies', methods=['POST'])
def read_cookies():
	content = request.get_json()
		# content is a DICTIONARY!

	for c in content['cookies']:
		keys = c.keys()
		values = c.values()
		# keys and values are LISTS

		if values[0] == 'www.'+ request.form['requested_domain']:
			cookie_object = Cookie()
			cookie_object.set_cookie_from_browser(c)
		        session.add(cookie_object)
			session.commit()

	# return jsonify(content)
	return redirect("/show_cookies.html")



@app.route('/welcome')
def welcome():
	return render_template("welcome.html")

@app.route('/search')
def search_cookies():
	return render_template("search.html")
	# return ""

@app.route('/set_browser_cookie')
def set_browser_cookie():

# REMEMBER: url and domain need to be THE SAME PLACE !!!

	return jsonify({"cookies": [
		{"url": "http://www.snaps.com", 
		"name": "testCookie3", 
		"value": "sample-value-here22",
		"domain": "snaps.com"}
		]
	})


@app.route('/call_cookies')
def call_cookies():
	# call cookies here
	return render_template("call_cookies.html")


@app.route('/show_cookies')
def show_cookies():
	# show cookies that are called above.
	return render_template("show_cookies.html")


################ stop cookie management


################ start development and test section




# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')



# @app.route('/view_cookies', methods=['POST'], ['GET'])
# def cookie_view():
# 	return "show me the cookies on your computer, returning user!"
	# existing user, see cookies there


################ stop development and test section


################ start app /websockets etc.


if __name__ == "__main__":
	# http_server = WSGIServer(('',5000), app, handler_class=WebSocketHandler)
	# http_server.serve_forever()
	app.run(debug=True)

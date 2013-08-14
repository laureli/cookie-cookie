import os
import json
from flask import Flask, render_template, send_from_directory, request, redirect, jsonify, g, flash, url_for, abort
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer

from model import Cookie, User, session
from forms import LoginForm

# DB config information
DATABASE = '/tmp/mixerapp.db' 

############## should i be using this one?
# DATABASE= "postgresql://mixerapp:mixerapp@localhost:5432/mixer"



DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin' 
PASSWORD = 'default'


# application
app = Flask(__name__)
app.config.from_object(__name__)

############### start websocket settings ###############

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


############### end websocket settings ###############

############### Start LoginHandler settings ###############

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

@lm.user_loader
def load_user(id):
    return session.query(User).get(int(id))

@app.before_request
def before_request():
    g.user = current_user
    # this is used as 'current_user.id' or 'current_user.email'
   

############### End LoginHandler settings ###############


############### start login / logout ###############

@app.route('/login', methods=['GET', 'POST'])
def login():
    # if user hasn't logged out redirect don't reload login page
    if current_user is not None and current_user.is_authenticated():
        return redirect(url_for('home'))

    form = LoginForm()  

    if form.validate_on_submit():
        user= session.query(User).filter_by(email=form.email.data, password=form.password.data).first()
    
        if user is not None:
            login_user(user)
            flash('Welcome')
        else:
            flash('Invalid login')

        return redirect(url_for('home'))
        
    return render_template('login.html',
                            title='Sign In',
                            form=form)


@app.route('/logout')
@login_required
def logout():
    session.pop('email', None)
# REDIRECT BACK TO THE SPLASH PAGE
    return render_template('/index')


@app.route('/home', methods=['GET', 'POST']) # index!
def home():
	# splash page for not-logged in users arriving not from extension
	# send to _login_ if you are a returning user
	# send to _sign up_ for new users
	return render_template('home.html',
		title='home')

############### end login / logout ###############


############### start managing users on website ###############

@app.route('/')
def redir():
	return redirect(url_for('login'))

@app.route('/index') # index!
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



@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
	return render_template("welcome.html",
		header = 'welcome'
		)

@app.route('/stats')
def stats():
	return render_template('stats.html',
		header = 'stats')

################ end managing users on website ###############


################ start managing extension ###############

# LOAD_COOKIES IS ONLY GETTING USED TO LOAD COOKIES INTO THE DATABASE RIGHT NOW
### LOAD_COOKIES can parse upload when the conditional statement is running.
#######  validate data in models.py	

@app.route('/load_cookies', methods=['POST', 'GET'])
def load_cookies():
	content = request.get_json()
		# content is a DICTIONARY!

	for c in content['cookies']:
		keys = c.keys()
		values = c.values()
		# keys and values are LISTS

		# if values[0] == 'www.'+ request.form['requested_domain']:
		cookie_object = Cookie()
		cookie_object.add_cookie_from_browser(c, current_user)
	        session.add(cookie_object)	
		session.commit()

	# return jsonify(content)
	# return redirect("/show_cookies.html")
	return 'confirmed, cookies loaded.'
# LOAD COOKIES IS USED TO LOAD COOKIES INTO THE DATABASE RIGHT NOW



@app.route('/show_cookies', methods=['GET'])
def show_cookies():
	# show cookies that are called above.
	data = Cookie.query.all()
	dbCookies = [d.__dict__ for d in data]

	return json.dumps(jsonify(dbCookies=dbCookies))




################ stop managing extension ###############






@app.route('/search')
def search_cookies():
	return render_template('search.html',
		header = 'search results'
		)
	# return '


@app.route('/set_browser_cookie')
def set_browser_cookie():

# REMEMBER: url and domain need to be THE SAME PLACE !!!

	return jsonify({'cookies': [
		{'url': 'http://www.snaps.com', 
		'name': 'testCookie3', 
		'value': 'sample-value-here22',
		'domain': 'snaps.com'}
		]
	})


@app.route('/call_cookies')
def call_cookies():
	# call cookies here
	return render_template('call_cookies.html')





################ start development & test section ###############


# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')


# @app.route('/view_cookies', methods=['POST'], ['GET'])
# def cookie_view():
# 	return "show me the cookies on your computer, returning user!"
	# existing user, see cookies there


################ stop development and test section ###############


################ start app, websockets, infrastructure ###############

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html', 
    	header='404 error'), 404


if __name__ == '__main__':
	# http_server = WSGIServer(('',5000), app, handler_class=WebSocketHandler)
	# http_server.serve_forever()
	app.run(debug=True)

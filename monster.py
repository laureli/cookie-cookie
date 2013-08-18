import os
import json
from flask import Flask, render_template, send_from_directory, request, redirect, jsonify, g, \
session, flash, url_for, abort
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer


from model import Cookie, User, dbsession
from forms import LoginForm, SignupForm

# DB config information  ## postgres address: "postgresql://mixerapp:mixerapp@localhost:5432/mixer"
DATABASE = '/tmp/mixerapp.db' 
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin' 
PASSWORD = 'default'


# application
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key= SECRET_KEY

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
    return dbsession.query(User).get(int(id))

@app.before_request
def before_request():
    g.user = current_user
    # this is used as 'current_user.id' or 'current_user.email'
   

############### End LoginHandler settings ###############


############### start login / logout ###############

@app.route('/login', methods=["GET", "POST"])
def login():
    # if user hasn't logged out redirect don't reload login page
    if current_user is not None and current_user.is_authenticated():
        return redirect(url_for('home'))

    form = LoginForm()  
    if form.validate_on_submit():

        user= dbsession.query(User).filter_by(email=form.email.data, password=form.password.data).first()
    
        if user is not None:
            login_user(user)
            session['email']=user.email
            session['user_id']=user.id
            session['username']=user.username
            flash("Welcome")
        else:
            flash("Invalid login")

        return redirect(url_for('home'))
    
    return render_template('login.html',
                            header='Sign In',
                            form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
# use ln 92 instead of 90 to get more control over login process
    # session.pop('email', None) 
    return redirect('/')


@app.route('/home', methods=['GET', 'POST']) # index!
@login_required
def home():
	# splash page for logged in users
	# send to _login_ if you are a returning user
	# send to _sign up_ for new users
	if 'email' not in session:
		return redirect(url_for('signup'))

	user = User.query.filter_by(email=session['email']).first()

	if user is None:
		return redirect(url_for('signin'))
	else:
		return render_template('home.html', 
								title='home')



############### end login / logout ###############

############### start managing users on website ###############


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form= SignupForm()

	if form.validate_on_submit():
	# check if email already exists
		email_exists = dbsession.query(User).filter_by(email = form.email.data).first()
	
		if email_exists != None:
			flash('Email already exists')
			return render_template('signup.html', 
				                    header='signup', 
				                    form=form)
		else:
			user = dbsession.add(User(username= form.username.data,
								  email= form.email.data,
								  password= form.password.data))
		    # add user
			dbsession.commit()

			flash("Registration almost done. Login to complete.")
		   	#user must login with new email/password
			return redirect(url_for('login'))

	return render_template('signup.html',
							header='signup',
							form=form)


@app.route('/stats')
def stats():
	return render_template('stats.html',
		header = 'stats')


@app.route('/welcome', methods=['GET', 'POST'])
@login_required
def welcome():
	return render_template("welcome.html",
		header = 'welcome'
		)


################ end managing users on website ###############

################ start managing extension ###############


# LOAD_COOKIES IS GETTING USED TO LOAD COOKIES INTO THE DATABASE
### LOAD_COOKIES can parse upload when the conditional statement is running.
#######  validate data in models.py	

@app.route('/load_cookies', methods=['POST'])
def load_cookies():
	content = request.get_json()
		# content is a DICTIONARY!

	for c in content['cookies']:
		keys = c.keys()
		values = c.values()
		# keys and values are LISTS

		# if values[0] == 'www.'+ request.form['requested_domain']:
		cookie_object = Cookie()
		cookie_object.add_cookie_from_browser(c)
		cookie_object.user_id=session['user_id']
		dbsession.add(cookie_object)
		dbsession.commit()

	return "confirmed, cookies loaded."


# SHOW_COOKIES GETS COOKIES FROM DB AND DISPLAYS @ EXTENSION

@app.route('/show_cookies', methods=['GET', 'POST'])
def show_cookies():
	data = Cookie.query.all()
	dbCookies = [d.json for d in data]
	return jsonify(dbCookies=dbCookies)


# REMEMBER:  SET_BROWSER_COOKIE -- url and domain need to be THE SAME PLACE !!!

@app.route('/set_browser_cookie')
def set_browser_cookie():
	return jsonify({"cookies": [
		{"url": "http://www.snaps.com", 
		"name": "testCookie3", 
		"value": "sample-value-here22",
		"domain": "snaps.com"}
		]
	})


################ stop managing extension ###############

################ start general navigation ###############


@app.route('/') # index!
def index_redir():
	return render_template('index.html')


@app.route('/search')
def search_cookies():
	return render_template("search.html",
		header = 'search results'
		)
	# return ""


@app.route('/call_cookies')
def call_cookies():
	# call cookies here
	return render_template("call_cookies.html")



################ stop general navigation ###############


################ start development & test section ###############


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/view_cookies', methods=['GET', 'POST'])
def cookie_view():
	return render_template('aaaaaaa.html')


################ stop development and test section ###############


################ start app, websockets, infrastructure ###############


# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page_not_found.html', 
#     	header='404 error'), 404


if __name__ == "__main__":
	# http_server = WSGIServer(('',5000), app, handler_class=WebSocketHandler)
	# http_server.serve_forever()
	app.run(debug=True)

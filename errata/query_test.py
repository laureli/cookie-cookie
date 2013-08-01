
# do some queries and make stuff happen!
import model 

user_list = model.session.query(model.user).all()
print user_list





actual steps.

PROBLEM: i am missing the "machine_id" in my postgres table. FIX THIS.


at command line:
	python -i model.py 

in the interactive python shell,
	session = connect()
	c = session.query(User).get(1)
	-> the above should get the first user in the database table...
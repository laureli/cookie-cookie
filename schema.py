
class User(Base):
	__tablename__="Users"
		id = Column(Integer, primary_key=True)
		username = Column(String)
		email = Column(String)
		password = Column(String)
		machine_id = Column(Integer)


class Cookie(Base):
	__tablename__="Cookies"
		id = Column(Integer, primary_key=True)
		name = Column(String) 
		value = Column()
		domain = Column()
		path = Column()
		expiration = Column()
		size = Column()
		http = Column()
		secure = Column()

################ below is the code inserted into the engine.

class User(Base):
	__tablename__="Users"
	id = Column(Integer, primary_key=True)
	username = Column(String(65))
	email = Column(String(255)) # check the limit in standards for email
	password = Column(String(65))


class Cookie(Base):
	__tablename__="Cookies"
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer)
	name = Column(String(100)) 
	value = Column(String(2000))
	domain = Column(String(254))
	path = Column(String(254))
	expiration = Column(DateTime())
	size = Column(Integer)
	http = Column(Boolean())
	secure = Column(Boolean())


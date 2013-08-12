from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import DateTime
from sqlalchemy.orm import sessionmaker, scoped_session

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref


engine = create_engine("postgresql://mixerapp:mixerapp@localhost:5432/mixer", echo=False)
session = scoped_session(sessionmaker(bind=engine,
                                autocommit=False,
                                autoflush=False))

Base = declarative_base()
Base.query = session.query_property()

class User(Base):
	__tablename__="users"
	id = Column(Integer, primary_key=True)
	username = Column(String(65))
	email = Column(String(255)) # check the limit in standards for email
	password = Column(String(65))

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<User %r>' % (self.username)

class Cookie(Base):
	__tablename__="cookies"
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer)
	name = Column(String(100)) 
	value = Column(String(2000))
	domain = Column(String(254))
	path = Column(String(254))
	expiration = Column(String(254))
	http = Column(Boolean())
	secure = Column(Boolean())


	def set_cookie_from_browser(self, c): # class instantiated @ monster.py
	  # include IF statements for data validation here
		self.name = c['name']
		self.value = c['value']
		self.domain = c['domain']
		self.path = c['path']
		self.http = c['httpOnly']
		self.secure = c['secure']
  		print 'the domain is', c['domain']


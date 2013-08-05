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


class Cookie(Base):
	__tablename__="cookies"
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


	def set_cookie_from_browser(c): # class instantiated @ monster.py
		# include validating if statements here
		self.name = c['name'],
		self.value = c['value'],
        self.domain = c['domain'],
        path = c['path'],
        http = c['httpOnly'],
        secure = c['secure']



        # correct table; not dealing with two columns:
        	# expiration = values[6],
	        # size = values[0],

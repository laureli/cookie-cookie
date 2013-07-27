from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# EXPLANATION OF DB call: 'postgresql://user:password@localhost/database
# engine = create_engine('postgresql://mixerapp:mixerapp@localhost:5432/mixer')

# session = scoped_session(sessionmaker(bind=engine,
#                                 autocommit=False,
#                                 autoflush=False))
def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("postgresql://mixerapp:mixerapp@localhost:5432/mixer", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()

# session = Session()

Base  =declarative_base()
# Base.query = session.query_property()


### Class declarations go here

class User(Base):
	__tablename__="users"
	id = Column(Integer, primary_key=True)
	username = Column(String(65))
	email = Column(String(255)) # check the limit in standards for email
	password = Column(String(65))
#	machine_id = Column(Integer)
	# -> machine_id not currently in the database table

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


### End class declarations

def main():
    """In case we need this for something"""
    pass




if __name__ == "__main__":
    main()
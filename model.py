from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import create_engine


# EXPLANATION OF DB call: 'postgresql://user:password@localhost/database
# engine = create_engine('postgresql://mixer:mixer@localhost:5432/mixer', echo=False)

# session = scoped_session(sessionmaker(bind=engine,
#                                 autocommit=False,
#                                 autoflush=False))


Base = declarative_base()
# Base.query = session.query_property()


### Class declarations go here

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


### End class declarations

def main():
    """In case we need this for something"""
    pass




if __name__ == "__main__":
    main()
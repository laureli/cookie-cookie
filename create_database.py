from sqlalchemy import create_engine
import model

engine = create_engine('postgresql://mixerapp:mixerapp@localhost:5432/mixer')
# user:password@localhost/database

Base.metadata.create_all(engine)






# making user and granting privileges on
# 	postgres=# create user mixerapp with password 'mixerapp';
# 	postgres=# grant all privileges on database mixer to mixerapp;

# actually signing into database:
# at command prompt:
# 	laureli@mini-u-box:~$ psql -d mixer -U mixerapp -h localhost
# 	password: mixerapp
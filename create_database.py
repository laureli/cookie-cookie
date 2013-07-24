from sqlalchemy import create_engine
import model

engine = create_engine('postgresql://mixer:mixer@localhost:5432/mixer')
# user:password@localhost/database

Base.metadata.create_all(engine)

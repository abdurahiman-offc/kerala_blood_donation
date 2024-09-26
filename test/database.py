from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


url = "postgresql://postgres:arkt123@localhost/my_pgdb"


engine = create_engine(url)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
sql_base = declarative_base()





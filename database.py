import psycopg2
from dotenv import dotenv_values
import psycopg2.extras



def connect():
    config = dict(dotenv_values('.env'))
    print(config)
    try:
        conn = psycopg2.connect(**config,cursor_factory=psycopg2.extras.RealDictCursor)
        if conn:
            return conn
    except(psycopg2.DatabaseError) as error:
       print(error)
    
connect()


# we use orm to interact with database, implemented using sqlalchamy

# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:arkt123@localhost/my_pgdb"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()
      
    
    


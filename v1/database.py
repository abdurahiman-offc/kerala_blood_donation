from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


url = "postgresql://postgres:arkt123@localhost/my_pgdb"


engine = create_engine(url)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
sql_base = declarative_base()





# import psycopg2
# from dotenv import dotenv_values
# import os

# import psycopg2.extras
# pt = os.path.join(os.path.dirname(__file__),'..','.env')


# def db_connect():
#     config = dict(dotenv_values(pt))
    
#     try:
#         conn = psycopg2.connect(**config,cursor_factory=psycopg2.extras.RealDictCursor)
#         if conn:
#             return conn
#     except(psycopg2.OperationalError) as error:
#             print(error,'connection failed')
            

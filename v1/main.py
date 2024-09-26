from fastapi import FastAPI

import psycopg2
from . import crud


 

# app = FastAPI()

# @app.get('/')
def root():
    
    res = crud.get_hospitals()
    print(res)
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from collections import defaultdict
from typing import Dict
from pydantic import BaseModel, EmailStr
import pandas as pd
from schema import Hospital,Blood_units,BBaction,Individual
import numpy as np
import crud




app = FastAPI()



@app.get('/')
def root():
    
    return {'message':'main page'}

@app.get('/profiles')
def get_profiles():
    res = crud.get_profile_details()
    return res

@app.get('/get_hospitals')
def get_hospitals():
    res = crud.get_hospital_details()
    return res

@app.get('/get_blood_bank/{hospital_id}')
def request_blood(hospital_id:int):
    res = crud.get_bloodbank(hospital_id)
    return res



@app.post('/add_profile')
def add_profile(profile:Individual): 
        res = crud.add_profile(profile)
        
 
        return {'message': res}

@app.post('/register_hospital')
async def register_hospital(val:Hospital):
    res = crud.add_hospital(val)
    return{'message': res}        




        
@app.put('/update_blood_bank/{hospital_id}')
def update_blood_bank(hospital_id:int,new_update:Blood_units,action:str):
    res = crud.update_bloodbank(hospital_id,new_update,action)
    return res
            
            
        
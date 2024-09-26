from pydantic import BaseModel,PositiveInt,EmailStr
from enum import Enum



class Blood_group(str,Enum):
    Ap = 'A+ve'
    ABp = 'AB+ve'
    Bp = 'B+ve'
    Op = 'O+ve'
    An =  'A-ve'
    ABn  ='AB-ve'
    Bn  = 'B-ve'
    On  = 'O-ve'

class tcase(BaseModel):
    
    name: str
    phone:str
    
    class Config:
        orm_mode = True
        
class Blood_donors(BaseModel):
    
    name:str
    age:int =PositiveInt
    gender:str
    blood_group:Blood_group
    weight: int
    phone:str
    place:str
    pin_code:str
    
    class Config:
        orm_mode = True
        
class Hospital(BaseModel):
    reg_id: int
    name: str
    place : str
    phone : int
    email : EmailStr
    pin_code:int
    
class BBaction(str,Enum):
    ADD = 'add'
    REMOVE = 'remove'
    
class Blood_units(BaseModel):

    a_pos  :PositiveInt|int=0
    ab_pos :PositiveInt|int=0
    b_pos  :PositiveInt|int=0
    o_pos  :PositiveInt|int=0
    a_neg  :PositiveInt|int=0
    ab_neg :PositiveInt|int=0
    b_neg  :PositiveInt|int=0
    o_neg  :PositiveInt|int=0
   
    def __add__(self,other):
        if isinstance(other,Blood_units):
            operable = {}
            for i in self.model_fields_set:
                operable[i] = self.__getattribute__(i) - other.__getattribute__(i)
            return Blood_units(**operable)
        return NotImplemented
    
    def __sub__(self,other):
        if isinstance(other,Blood_units):
            nonoperable ={}
            operable = {}
            for i in self.model_fields_set:
                if self.__getattribute__(i) < other.__getattribute__(i):
                    nonoperable[i] = other.__getattribute__(i)
                else:
                    operable[i] = self.__getattribute__(i) - other.__getattribute__(i)
            if nonoperable:
                raise ValueError(f'new values are higher than previous {nonoperable}')
    
            return Blood_units(**operable)
        return NotImplemented

    
from pydantic import BaseModel,EmailStr,Field,PositiveInt
from enum import Enum
from typing import Literal


class Blood_group(str,Enum):
    Ap = 'A+ve'
    ABp = 'AB+ve'
    Bp = 'B+ve'
    Op = 'O+ve'
    An =  'A-ve'
    ABn  ='AB-ve'
    Bn  = 'B-ve'
    On  = 'O-ve'
     
# schemas for hospital blood bank update
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
            
            return Blood_units( a_pos=self.a_pos+other.a_pos,
                                ab_pos=self.ab_pos+other.ab_pos,
                                b_pos=self.b_pos+other.b_pos,
                                o_pos=self.o_pos+other.o_pos,
                                a_neg=self.a_neg+other.a_neg,
                                ab_neg=self.ab_neg+other.ab_neg,
                                b_neg=self.b_neg+other.b_neg,
                                o_neg=self.o_neg+other.o_neg)
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
            # return Blood_units( a_pos=self.a_pos-other.a_pos,
            #                     ab_pos=self.ab_pos-other.ab_pos,
            #                     b_pos=self.b_pos-other.b_pos,
            #                     o_pos=self.o_pos-other.o_pos,
            #                     a_neg=self.a_neg-other.a_neg,
            #                     ab_neg=self.ab_neg-other.ab_neg,
            #                     b_neg=self.b_neg-other.b_neg,
            #                     o_neg=self.o_neg-other.o_neg)
            return Blood_units(**operable)
        return NotImplemented
    
    
    
    
class Individual(BaseModel):
    name:str
    age:PositiveInt
    blood_group:Blood_group
    pho_nege:PositiveInt
    place:str
    pin_code:int
    weight: int
    gender:str
    
    
# schema for hospital details registration
class Hospital(BaseModel):
    name: str
    reg_id: int
    place : str
    pin_code:int
    phone : int
    email : EmailStr
    
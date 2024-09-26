import uuid
from .database import sql_base
from sqlalchemy import Column,Integer,String,CheckConstraint,CHAR
from sqlalchemy.dialects.postgresql import UUID as id_uuid

class test_table(sql_base):
    __tablename__ = "testcase"
    
    id = Column(id_uuid(as_uuid=True),primary_key=True,default=uuid.uuid4)
    name = Column(String,nullable=False)
    phone = Column(String,nullable=False)
    

class Blood_donors_details(sql_base):
    __tablename__="blood_donors_details"
    
    id = Column(id_uuid(as_uuid =True),primary_key=True,default=uuid.uuid4)
    name = Column(String)
    age = Column(Integer,nullable=False)
    gender = Column(CHAR(1),nullable=False)
    blood_group = Column(String,nullable=False)
    weight = Column(Integer,nullable=False)
    phone = Column(String,nullable=False)
    place = Column(String,nullable=False)
    pin_code = Column(String,nullable=False)  
    
    __table_args__ = (
        CheckConstraint('age > 17'),
        CheckConstraint('weight > 60')
    ) 
    
class Hospitals(sql_base):
    
    __tablename__ = "hospital_details"
    
    reg_id = Column(Integer,primary_key=True)
    name = Column(str,nullable=False)
    place = Column(str,nullable=False)
    phone = Column(str,nullable=False)
    email = Column(str,nullable=False)
    pin_code = Column(str,nullable=False)
    
class Blood_units(sql_base):
    __tablename__ = "blood_units"
    
    hospital_id = Column(Integer,unique=True,nullable=False)
    a_pos  = Column(Integer,nullable= False)
    ab_pos = Column(Integer,nullable= False)
    b_pos  = Column(Integer,nullable= False)
    o_pos  = Column(Integer,nullable= False)
    a_neg  = Column(Integer,nullable= False)
    ab_neg = Column(Integer,nullable= False)
    b_neg  = Column(Integer,nullable= False)
    o_neg  = Column(Integer,nullable= False)
    
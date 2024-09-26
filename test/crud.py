from sqlalchemy.orm import Session
from sqlalchemy import select
from . import models,schemas



def add_test(dt:schemas.tcase,db:Session):
    get_data = dt.model_dump()
    data = models.test_table(**get_data)
    with db:
        try:
            db.add(data)
            db.commit()
        except Exception as e:
            print(str(e))
            return "not added, error in db"
    return "added"

def add_donors(dt:schemas.Blood_donors,db:Session):
    get_data = dt.model_dump()
    data = models.Blood_donors_details(**get_data)
    with db:
        try:
            db.add(data)
            db.commit()
        except Exception as e:
            print(str(e))
            return "error in db"
    return "added"
    
    
    
    
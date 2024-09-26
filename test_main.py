from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from test import crud,models,schemas
from test.database import session_local,engine


models.sql_base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
        
@app.get('/')
def root():
    return "ok"


@app.post('/post_test')
def post_test(data:schemas.tcase,db:Session = Depends(get_db)):
    res = crud.add_test(data,db)
    return res

@app.post('/post_donors')
def post_donors(dt:schemas.Blood_donors,db:Session=Depends(get_db)):
    res = crud.add_donors(dt,db)
    
    return res
  



from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from v1 import crud
from v1 import schemas

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/',response_class=HTMLResponse)
def root(request:Request):
    return templates.TemplateResponse(request=request,name="index.html")

@app.get('/donors',response_class=HTMLResponse)
def get_donors(request:Request):
    res = crud.get_donors()
    if res is None:
        raise HTTPException(status_code=404,detail='no database connection')
    return res
    # return templates.TemplateResponse(request=request,name = "index.html",context={"title":"blood bank system","donors":res})

@app.get('/donors/{blood_group}')
def get_donors(blood_group: schemas.Blood_group):
    res = crud.get_donors(blood_group)
    if res is None:
        raise HTTPException(status_code=404,detail='no database connection')
    else:
        return res

@app.get('/hospitals')
def get_hospitals():
    res = crud.get_hospitals()
    if res is None:
        raise HTTPException(status_code=404,detail='no database connection')
    else:
        return res
    
    


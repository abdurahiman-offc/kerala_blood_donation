import psycopg2
from .database import session_local
from . import schemas


def donors():
    db = session_local()
    db.query()

def get_donors(blood_group:schemas.Blood_group=None):
    if blood_group:
        command = "SELECT * FROM blood_donors WHERE blood_group = %s "
        values = (blood_group,)
        db = db_connect()
        if db:
            try:
                with db.cursor() as curr:
                    curr.execute(command,values)
                    table = curr.fetchone()

            except psycopg2.Error as error:
                print(error)
            finally:
                if db:
                    db.close()
            if table:
                return table
            
    else:
        command = "SELECT * FROM blood_donors"
        db = db_connect()
        if db:
            try:
                with db.cursor() as curr:
                    curr.execute(command)
                    table = curr.fetchall()

            except psycopg2.Error as error:
                print(error)
            finally:
                if db:
                    db.close()
            if table:
                return table
        

def get_hospitals():
    command = "SELECT * FROM hospitals"
    db = db_connect()
    if db:
        try:
            with db.cursor() as curr:
                curr.execute(command)
                table = curr.fetchall()
                
        except psycopg2.Error as error:
            print(error)
        finally:
            if db:
                db.close()
        if table:
            return table
    # else:
    #     raise psycopg2.OperationalError('no database connection')
    
    # return table


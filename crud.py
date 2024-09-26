import psycopg2
import psycopg2.extras
from database import connect
from schema import Individual,Hospital,Blood_units,BBaction


def get_profile_details():
    
    command = "SELECT * FROM blood_donors;" 
    
    try :
        db = connect()
    except psycopg2.DatabaseError as e:
        print('-----',e)
    if db:
        try:
            with db.cursor() as curr:
                curr.execute(command)
                table = curr.fetchall() 
                
        except (psycopg2.DatabaseError,psycopg2.ProgrammingError) as e:
            print('-----',e)
        finally:
            db.close()
    else:
        raise psycopg2.DatabaseError('database not connected')
    print(table)
    return table

def add_profile(profile:Individual):
    profile_detail = profile.model_dump()
    info = tuple(profile_detail.values())
        
    command = """
    INSERT INTO profile (name,age,blood_group,phone,place,pin,weight,gender)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """
    try :
        db = connect()
    except psycopg2.DatabaseError as e:
        print('-----',e)
    if db:
        try:
            with db.cursor() as curr:
                curr.execute(command,info)
            db.commit()
        except (psycopg2.DatabaseError,psycopg2.ProgrammingError) as e:
            print('-----',e)
        finally:
            db.close()
    else:
        raise psycopg2.DatabaseError('database not connected')

    return 'profile added'          


def get_hospital_details():
    
    command = "SELECT * FROM hospitals;" 
    
    try :
        db = connect()
    except psycopg2.DatabaseError as e:
        print('-----',e)
    if db:
        try:
            with db.cursor() as curr:
                curr.execute(command)
                table = curr.fetchall() 
        except (psycopg2.DatabaseError,psycopg2.ProgrammingError) as e:
            print('-----',e)
        finally:
            db.close()
    else:
        raise psycopg2.DatabaseError('--database not connected')
    return table



def add_hospital(details:Hospital):
    hospital_details = details.model_dump()
    info = tuple(hospital_details.values())
    bb_val = (hospital_details['reg_id'],0,0,0,0,0,0,0,0)
    
    command = """INSERT INTO hospitals (name,reg_id,place,pin_code,phone,email)
              VALUES (%s,%s,%s,%s,%s,%s)  
    """
    create_bb = """INSERT INTO bb_update (reg_id,a_pos,ab_pos,b_pos,o_pos,a_neg,ab_neg,b_neg,o_neg)
              VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)  
    """
    try :
        db = connect()
    except psycopg2.DatabaseError as e:
        print('-----',e)
    if db:
        try:
            with db.cursor() as curr:
                curr.execute(command,info)
                curr.execute(create_bb,bb_val)
            db.commit()   
        except (psycopg2.DatabaseError,psycopg2.ProgrammingError) as e:
            print('-----',e)
        finally:
            db.close()
    else:
        raise psycopg2.DatabaseError('database not connected')
    # print(table)
    return 'hospital added'

def get_bloodbank(reg_id:int):
    command = "SELECT * FROM bb_update WHERE reg_id = %s"
    param = (reg_id,)
    
    try :
        db = connect()
    except psycopg2.DatabaseError as e:
        print('-----',e)
    if db:
        try:
            with db.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as curr:
                curr.execute(command,param)
                value = curr.fetchone()
                
        except (psycopg2.DatabaseError,psycopg2.ProgrammingError) as e:
            print('-----',e)
        finally:
            db.close()
    else:
        raise psycopg2.DatabaseError('database not connected')
    # print(table)
    return dict(value)
    
    
    
def update_bloodbank(hospital_id:int,new_update:Blood_units,action:BBaction):
    
    if action == BBaction.ADD:
        try:
            old_val = get_bloodbank(hospital_id)
        except psycopg2.Error as e:
            print('no id found')
        old_val.pop('reg_id')
        old_val = Blood_units(**old_val)
        updated = old_val+new_update
        unpack_updated = updated.model_dump()
        # unpack_updated = tuple(unpack_updated.values())
        update_query = "UPDATE bb_update SET a_pos=%s,ab_pos=%s,b_pos=%s,o_pos=%s,a_neg=%s,ab_neg=%s,b_neg=%s,o_neg=%s WHERE reg_id = %s"
        param=(unpack_updated['a_pos'],unpack_updated['ab_pos'],unpack_updated['b_pos'],unpack_updated['o_pos'],
               unpack_updated['a_neg'],unpack_updated['ab_neg'],unpack_updated['b_neg'],unpack_updated['o_neg'],hospital_id)
        try :
            db = connect()
        except psycopg2.DatabaseError as e:
            print('-----',e)
        if db:
            try:
                with db.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as curr:
                    curr.execute(update_query,param)

                db.commit()   
            except (psycopg2.DatabaseError,psycopg2.ProgrammingError) as e:
                print('-----',e)
            finally:
                db.close()
        else:
            raise psycopg2.DatabaseError('database not connected')
        # print(table)

        return 'updated'
    # if action == BBaction.ADD:

    else:   
        try:
            old_val = get_bloodbank(hospital_id)
        except psycopg2.Error as e:
            print('no id found')
        old_val.pop('reg_id')
        old_val = Blood_units(**old_val)
        updated = old_val-new_update
        unpack_updated = updated.model_dump()
        # unpack_updated = tuple(unpack_updated.values())
        update_query = "UPDATE bb_update SET a_pos=%s,ab_pos=%s,b_pos=%s,o_pos=%s,a_neg=%s,ab_neg=%s,b_neg=%s,o_neg=%s WHERE reg_id = %s"
        param=(unpack_updated['a_pos'],unpack_updated['ab_pos'],unpack_updated['b_pos'],unpack_updated['o_pos'],
               unpack_updated['a_neg'],unpack_updated['ab_neg'],unpack_updated['b_neg'],unpack_updated['o_neg'],hospital_id)
        try :
            db = connect()
        except psycopg2.DatabaseError as e:
            print('-----',e)
        if db:
            try:
                with db.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as curr:
                    curr.execute(update_query,param)
                    
                db.commit()   
            except (psycopg2.DatabaseError,psycopg2.ProgrammingError) as e:
                print('-----',e)
            finally:
                db.close()
        else:
            raise psycopg2.DatabaseError('database not connected')
        # print(table)
        
        return 'updated'
    
    




    
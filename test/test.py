from database import connect

command = "INSERT INTO employee (%s,%s,%s VALUES (%s,%s,%s)"
val =(34,'ff','d2')
with connect() as conn:
    with conn.cursor() as curr:
         curr.execute(command,val)
         conn.commit()

print(curr)         
print(conn)
    
# try :
#     conn = connect()
#     curr = conn.cursor()
#     curr.execute(command,val)
#     conn.commit()
# except:
#     print('error')
# finally:
#     conn.close()
    
# print(conn)
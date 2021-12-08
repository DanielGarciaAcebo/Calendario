# own imports
import main


#def of profile
def get_profile(id):
    conexion = main.conect()
    with conexion.cursor() as cursor:
        usuarios = cursor.execute('''SELECT * FROM USER WHERE ID=id ''')
    conexion.commit()
    conexion.close()
    return usuarios

def updateProfile():
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute(f"UPDATE")
    conexion.commit()
    conexion.close()
# ----------------------------------------------------------------------------------------------------

# Def of grow and seeds
def grow():
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT SEED_ID, "
                       "NAME, DESCRIPTION, "
                       "DAYTIME,DAYCOLLECTION, "
                       "DATE_FORMAT(FINALDAY,'%d-%m'),"
                       "DATE_FORMAT(STARTDAY, '%d-%m')"
                       " FROM SEED")
        seeds = cursor.fetchall()
    conexion.commit()
    conexion.close()
    return seeds

# ------------------------------------------------------------------------------------------------------
#def of contacts
def companies():
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT * FROM TYPE_COMPANY WHERE COMPANY_TYPE != 0")
        companies = cursor.fetchall()
    conexion.commit()
    conexion.close()
    return companies

def contacts(companyID):
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT COMPANY_ID, NAME, CITYHALL  FROM company WHERE COMPANY_ID = %s", (companyID,))
        contacts = cursor.fetchall()
    conexion.commit()
    conexion.close()
    return contacts

def contact(contactID):
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT NAME, SURNAME, EMAIL, NUMBERTF FROM USERS WHERE COMPANY_TYPE = %s", (contactID,) )
        contacts = cursor.fetchall()
    conexion.connection.commit()
    conexion.close()
    return contacts


# ---------------------------------------------------------------------------------------------
#def of task
def get_taks(ID):
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT NOTES_ID,  NAME, COMMENT, DATE_FORMAT(DATE,'%d-%m-%y') "
                       f"FROM TASK WHERE USER=%s", (ID,))
        tasks = cursor.fetchall()
    conexion.commit()
    conexion.close()
    return tasks

def set_task( userID, name, comment, date ):
    conexion = main.conect()
    with conexion.cursor() as cursor1:
        cursor1(f"SELECT NOTES_ID +1 FROM TASK ORDER BY NOTES_ID DESC LIMIT 1")
        noteID = cursor1.fetchone()
    with conexion.cursor() as cursor2:
        cursor2.execute(f"INSERT INTO TASK (NOTES_ID, NAME, COMMENT, DATE_FORMAT(DATE,'%d-%m-%y'), USER) "
                        f"VALUES(%s,%s,%s,%s,%s)", (noteID, name, comment, date, userID))
    conexion.commit()
    conexion.close()

def update_task(noteID, userID, name, comment, date ):
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute(f"UPDATE  (NAME,COMMENT,DATE,USER) FROM TASK WHERE NOTES_ID=%s", (name, comment, date, userID,), (noteID,))
        cursor.fetchall()
    conexion.commit()
    conexion.close()

def delete_task(userID, taskID):
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute(f"DELETE FROM TASK WHERE NOTES_ID=%s AND USER= %s", (taskID, userID))
        cursor.fetchall()
    conexion.commit()
    conexion.close()




# own imports
import main


# Def of profile
def get_user_profile(id):
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM USER WHERE USER_ID = %s", (id,))
        usuarios = cursor.fetchone()
    conexion.commit()
    conexion.close()
    return usuarios


def get_company_profile(id):
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute('SELECT * FROM COMPANY WHERE ID_COMPANY = %s', (id))
        usuarios = cursor.fetchone()
    conexion.commit()
    conexion.close()
    return usuarios


def get_type_company_profile(id):
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute('SELECT * FROM TYPE_COMPANY WHERE COMPANY_TYPE_ID = %s', (id))
        usuarios = cursor.fetchone()
    conexion.commit()
    conexion.close()
    return usuarios

# ----------------------------------------Def of grow and seeds----------------------------------------------
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


# -----------------------------------------Def of contacts-------------------------------------------------------------

def get_companies():
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT * FROM TYPE_COMPANY WHERE COMPANY_TYPE_ID != 0")
        companies = cursor.fetchall()
    conexion.commit()
    conexion.close()
    return companies


def get_contacts(companyID):
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT ID_COMPANY, NAME_COMPANY, CITYHALL  FROM COMPANY WHERE COMPANY_TYPE_ID = %s", (companyID,))
        contacts = cursor.fetchall()
    conexion.commit()
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT *  FROM COMPANY WHERE USER")
        users = cursor.fetchall()
    conexion.commit()
    conexion.close()
    return main.render_template("contact.html", contacts=contacts, users=users)



# --------------------------------------------Def of Task-------------------------------------------------

def get_taks(ID):
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT NOTES_ID,NAME, COMMENT, DATE FROM TASK WHERE USER = %s", (ID,))
        tasks = cursor.fetchall()
    conexion.commit()
    conexion.close()
    return tasks

def set_task(userID, name, comment, date):
    conexion = main.conect()
    with conexion.cursor() as cursor1:
        cursor1(f"SELECT NOTES_ID +1 FROM TASK ORDER BY NOTES_ID DESC LIMIT 1")
        noteID = cursor1.fetchone()
    with conexion.cursor() as cursor2:
        cursor2.execute(f"INSERT INTO TASK (NOTES_ID, NAME, COMMENT, DATE, USER) "
                        f"VALUES(%s,%s,%s,%s,%s)", (noteID, name, comment, date, userID))
    conexion.commit()
    conexion.close()
    return main.redirect(main.url_for("tasks"))


def set_update_task(noteID, userID, name, comment, date):
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute(f"UPDATE TASK SET  NAME=%s, COMMENT=%s, DATE=%s, USER=%s WHERE NOTES_ID=%s ",
                       (name, comment, date, userID, noteID))
        cursor.fetchall()
    conexion.commit()
    conexion.close()


def get_update_task(noteID):
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT NOTES_ID, NAME, COMMENT, DATE FROM TASK WHERE NOTES_ID=%s", (noteID,))
        tasks = cursor.fetchone()
    conexion.commit()
    conexion.close()
    return tasks


def delete_task(userID, taskID):
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute(f"DELETE FROM TASK WHERE NOTES_ID=%s AND USER= %s", (taskID, userID))
        cursor.fetchall()
    conexion.commit()
    conexion.close()

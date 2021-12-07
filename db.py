# imports
from typing import List, Optional, Tuple, cast  # noqa: F401

# own imports
import main


#def of profile
def profile(id):
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



#def of task
def taks(ID):
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT * FROM TASK WHERE ID_CLIENTE=ID ")
        tasks = cursor.fetchall()
    conexion.commit()
    conexion.close()
    return tasks




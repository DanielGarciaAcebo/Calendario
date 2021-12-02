# imports
from typing import List, Optional, Tuple, cast  # noqa: F401

# own imports
import main


#def of profile
def profile(id):
    cursor = main.mysql.connection.cursor()
    usuarios = cursor.execute(f"SELECT * FROM USERS WHERE ID=id ")
    cursor.connection.commit()
    return usuarios

def updateProfile():
    cursor = main.mysql.connection.cursor()
    cursor.execute(f"UPDATE")
    cursor.connection.commit()


# Def of grow and seeds
def grow():
    cursor = main.mysql.connection.cursor()
    seed = cursor.execute(f"SELECT * FROM SEEDS ")
    cursor.connection.commit()
    return seed

def showSeeds(seeds):
    cursor = main.mysql.connection.cursor()
    cursor.execute(f"UPDATE")
    cursor.connection.commit()
    cursor = main.mysql.connection.cursor()
    dates = cursor.execute(f"SELECT * FROM SEEDS WHERE SHOW= TRUE ")
    cursor.connection.commit()
    return dates


#def of contacts
def contacts(id):
    cursor = main.mysql.connection.cursor()
    contacts = cursor.execute(f"SELECT * FROM USERS WHERE COMPANY_TYPE=ID ")
    cursor.connection.commit()
    return contacts

def conpanyContacts(companyID,contactID):
    cursor = main.mysql.connection.cursor()
    contacts = cursor.execute(f"SELECT * FROM USERS WHERE COMPANY_TYPE=ID ")
    cursor.connection.commit()
    return contacts

#def of task
def taks(ID):
    cursor = main.mysql.connection.cursor()
    tasks = cursor.execute(f"SELECT * FROM TASK WHERE ID_CLIENTE=ID ")
    cursor.connection.commit()
    return tasks




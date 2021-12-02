# imports
import MySQLdb
import flask_login
import main
from flask_login import login_manager,logout_user,UserMixin
from flask_login.login_manager import LoginManager


# Login
def login(mail, name, password):
    cursor = main.mysql.connection.cursor()
    usuarios = cursor.execute(f"SELECT * FROM USERS ")
    cursor.connection.commit()
    for usuario in usuarios:
        if usuario.NAME == name & usuario.MAIL == mail & usuario.PASSWORD == password:
            id = usuario.ID
            User(name, id, mail)

# register
def register(name,surname,number,email,password,company,companyName,cityHall):
    cursor = main.mysql.connection.cursor()

    try:
        cursor.execute(f"INSERT IN TO USERS (NAME, SURNAME, PASS, EMAIL, NUMBERTF, COMP) VALUES (name, surname, password, email, number, company)")
        cursor.execute(f"INSERT IN TO USERS (NAME, CITYHALL, COMPANYTYPE) VALUES ()")
        cursor.connection.commit()

    except:
        cursor.connection.commit()
        return ""

# Utilities
class User(UserMixin):
    def __init__(self, name, id, mail):
        self.id = id
        self.name = name
        self.mail = mail

def get_user(self):
    return self.id

#Login manager
def logging_in(app):
    lm = LoginManager()
    lm.user_loader(get_user)
    lm.setup_app(app)
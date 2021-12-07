# imports
import MySQLdb
import flask_login
import main
import forms
from flask_login import login_manager, logout_user, UserMixin
from flask_login.login_manager import LoginManager


# Login
def login(mail, name, password):
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT USER_ID, NAME, EMAIL, PASS FROM USER;")
        usuarios = cursor.fetchall()
    conexion.connection.commit()
    conexion.close()
    for usuario in usuarios:
        if usuario[1] == name & usuario[4] == mail & usuario[5] == password:
            id = usuario[0]
            User(name, id, mail)


# register
def register(name, surname, number, email, password, companyType, companyName, cityHall):
    conexion = main.conect()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(f"INSERT IN TO COMPANY (NAME, CITYHALL, COMPANYTYPE) VALUES (%s,%s,%s);", (companyName, cityHall, companyType))
            conexion.commit()
            cursor.execute(f"SELECT COMPANY_ID FORM COMPANY WHERE NAME = %s;", (companyName, ))
            company = cursor.fetchone()
            cursor.execute(f"INSERT INTO USER (NAME, PASS ,SURNAME, EMAIL, NUMBERTF, COMPANY, TASK_ID) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                           (name, surname, password, email, number, company, company, ))
            conexion.commit()
            cursor.execute(f"SELECT * FROM USER;")
            usuarios = cursor.fetchall()
        conexion.commit()
        conexion.close()
        for usuario in usuarios:
            if usuario.NAME == name & usuario.MAIL == email & usuario.PASSWORD == password:
                id = usuario.ID
                User(name, id, email)

    except:
        print("The def register its dead")
        form = forms.register(main.request.form)
        return main.render_template("register.html", form=form)


# Utilities
class User(UserMixin):
    def __init__(self, name, id, mail):
        self.id = id
        self.name = name
        self.mail = mail


def get_user(self):
    return self.id


# Login manager
def logging_in(app):
    lm = LoginManager()
    lm.user_loader(get_user)
    lm.setup_app(app)

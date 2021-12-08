# imports
import MySQLdb
import flask_login
import main
import forms
from ownApp import app
from flask_login import logout_user, UserMixin, LoginManager, login_user
from werkzeug.security import generate_password_hash

# app definition
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = "login"


def login(mail, name, password):
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT USER_ID, NAME, EMAIL, PASS FROM USER;")
        usuarios = cursor.fetchall()
    conexion.commit()
    conexion.close()
    for usuario in usuarios:
        if usuario[1] == name and usuario[2] == mail and usuario[3] == password:
            id = usuario[0]
            # creamos usuario
            user = User(str(id), str(name), str(mail), str(password))
            # Dejamos el usuario logeado
            login_user(user, remember=True)


# register
def register(name, surname, number, email, password, companyType, companyName, cityHall):
    conexion = main.conect()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(f"SELECT COMPANY_ID +1  FROM COMPANY ORDER BY COMPANY_ID DESC LIMIT 1")
            company = cursor.fetchone()
            cursor.execute(
                f"INSERT INTO USER (NAME, SURNAME, PASS, EMAIL, NUMBERTF, COMPANY, TASK_ID) VALUES (%s, %s, %s, %s, %s, %s, %s);",
                (name, surname, password, email, number, company, company))
            conexion.commit()
            cursor.execute(f"INSERT INTO COMPANY (NAME, CITYHALL, COMPANYTYPE) VALUES (%s,%s,%s);",
                           (companyName, cityHall, companyType))
            conexion.commit()
        conexion.close()
        login(email, name, password)
    except:
        print("The def register its dead")
        form = forms.register(main.request.form)
        return main.render_template("register.html", form=form)


# logout
def logout():
    logout_user()


# user instance
class User(UserMixin):
    def __init__(self, id, username, mail, userpass, is_admin=False):
        self.id = id
        self.name = username
        self.mail = mail
        self.password = generate_password_hash(userpass)
        self.is_admin = is_admin


@login_manager.user_loader
def load_user(id):
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT USER_ID, NAME, EMAIL, PASS FROM USER;")
        usuarios = cursor.fetchall()
    conexion.commit()
    conexion.close()
    for user in usuarios:
        if user[0]=="id":
            return user
    return None


@property
def is_active(self):
    return True


@property
def is_authenticated(self):
    return True


@property
def is_anonymous(self):
    return False
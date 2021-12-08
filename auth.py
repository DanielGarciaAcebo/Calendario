# imports
import main
import forms

# --------------------------------------------sesiones--------------------------
session = main.session

# ---------------------------------login-----------------------------------------
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
            # Creation session
            session["user_id"] = id
            session["user_name"] = name
            session["user_pass"] = password


# ------------------------------------------register--------------------------------------
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
   session.pop("user_id")
   session.pop("user_name")
   session.pop("user_pass")

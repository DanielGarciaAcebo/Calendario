# imports
import main
import forms

# --------------------------------------------sesiones--------------------------
session = main.session


# ---------------------------------login-----------------------------------------
def login(email, name, password):
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT USER_ID, NAME_USER, EMAIL, PASS FROM USER;")
        usuarios = cursor.fetchall()
    conexion.commit()
    conexion.close()
    for usuario in usuarios:
        if usuario[1] == name and usuario[2] == email and usuario[3] == password:
            id = usuario[0]
            print(id)
            # Creation session
            session["user_id"] = int(id)
            session["user_name"] = name
            session["user_pass"] = password
            return main.redirect((main.url_for("calendar")))
        else:
            return main.redirect(main.url_for("index"))

# ------------------------------------------register--------------------------------------
def register(name, surname, number, email, password, companyType, companyName, cityHall):
    conexion = main.conect()
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT USER_ID, NAME, EMAIL, PASS FROM USER;")
        usuarios = cursor.fetchall()
    conexion.commit()
    conexion.close()
    for usuario in usuarios:
        if usuario[1] == name and usuario[2] == email and usuario[3] == password:
            return main.redirect(main.url_for("login"))
        else:
            try:
                with conexion.cursor() as cursor:
                    cursor.execute(f"SELECT ID_COMPANY + 1  FROM COMPANY ORDER BY ID_COMPANY DESC LIMIT 1")
                    company = cursor.fetchone()
                    cursor.execute(
                        f"INSERT INTO USER (NAME_USER, SURNAME, PASS, EMAIL, NUMBERTF, COMPANY_ID, TASK_ID) VALUES (%s, %s, %s, %s, %s, %s, %s);",
                        (name, surname, password, email, number, company, company))
                    conexion.commit()
                    cursor.execute(
                        f"INSERT INTO COMPANY (ID_COMPANY ,NAME_COMPANY, CITYHALL, COMPANY_TYPE) VALUES (%s,%s,%s,%s);",
                        (company, companyName, cityHall, companyType))
                    conexion.commit()
                conexion.close()
                print("register accept")
                with conexion.cursor() as cursor:
                    cursor.execute(f"SELECT USER_ID, NAME_USER, EMAIL, PASS FROM USER;")
                    usuarios = cursor.fetchall()
                conexion.commit()
                conexion.close()
                for usuario in usuarios:
                    if usuario[1] == name and usuario[2] == email and usuario[3] == password:
                        id = usuario[0]
                        # Creation session
                        session["user_id"] = id
                        session["user_name"] = name
                        session["user_pass"] = password

            except:
                print("The def register its dead")
                form = forms.register(main.request.form)
                return main.render_template("register.html", form=form)


# logout
def logout():
    session.pop("user_id")
    session.pop("user_name")
    session.pop("user_pass")

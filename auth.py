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

    return main.redirect(main.url_for("index"))


# ------------------------------------------register--------------------------------------
def register(name, surname, number, email, password, companyType, companyName, cityHall):
    conexion = main.conect()
    with conexion.cursor() as cursor5:
        cursor5.execute(f"SELECT USER_ID, NAME_USER, EMAIL, PASS FROM USER;")
        usuarios = cursor5.fetchall()
    conexion.commit()
    conexion.close()
    for usuario in usuarios:
        if usuario[1] == name and usuario[2] == email and usuario[3] == password:
            main.flash("usuario ya registrado, inicie seesion")
            return main.redirect(main.url_for("index"))
        else:
            return continue_register(name, surname, number, email, password, companyType, companyName, cityHall)

def continue_register(name, surname, number, email, password, companyType, companyName, cityHall):
    conexion = main.conect()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT ID_COMPANY + 1  FROM COMPANY ORDER BY ID_COMPANY DESC LIMIT 1")
            company = cursor.fetchone()
        conexion.commit()
        conexion.close()
        print("compañia seleccionada")
        conexion.ping()
        with conexion.cursor() as cursor1:
            cursor1.execute(f"INSERT INTO USER (NAME_USER, PASS ,SURNAME, EMAIL, NUMBERTF, COMPANY_ID, TASK_ID) VALUES(%s, %s, %s , %s, %s, %s, %s);", (name, password, surname, email, number, company, company))
            conexion.commit()
        conexion.commit()
        conexion.close()
        print("user insert")
        conexion.ping()
        with conexion.cursor() as cursor2:
            cursor2.execute(
                f"INSERT INTO COMPANY ( ID_COMPANY, NAME_COMPANY, CITYHALL, COMPANY_TYPE) VALUES( %s, %s, %s, %s);",(company, companyName, cityHall, companyType))
        conexion.commit()
        conexion.close()
        print("register accept")

        return main.redirect(main.url_for("main_login"))
    except ValueError:
        print("The def register its dead")
        return main.render_template("index.html")


# logout
def logout():
    if session["user_id"]:
        session.pop("user_id")
        session.pop("user_name")
        session.pop("user_pass")
        return main.redirect(main.url_for("index"))
    else:
        return main.redirect(main.url_for("index"))

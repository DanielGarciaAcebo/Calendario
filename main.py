# imports
from typing import List, Optional, Tuple, cast  # noqa: F401

import os
import pymysql
from flask import redirect, render_template, request, flash, url_for, Flask, session
from werkzeug.wrappers import Response

# own imports
import auth
import db
import forms
from gregorian_calendar import GregorianCalendar


# ------------------------------Creation for debug------------------------------------------
app = Flask(__name__)

# ------------------------------Secret key------------------------------------------
secret_key = os.urandom(12)
app.secret_key = secret_key
app.config["SECRET_KEY"] = secret_key



# ---------------------------------connect DB-------------------------------------------
def conect():
    return pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="root",
                           db="calendariodb")


# ------------------------------ paginas de errores----------------------------------------------
@app.errorhandler(404)
def page_no_found(e):
    return render_template("404.html")


# --------------------------------------INDEX----------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")


# ---------------------------Login and registrer and logout-------------------------------------
@app.route("/login/")
@app.route("/login/", methods=["POST"])
def main_login():
    form = forms.login(request.form)
    if request.method == "POST" and form.validate():
        email = form.email.data
        name = form.name.data
        password = form.password.data
        return auth.login(email, name, password)
    else:
        return render_template("login.html", form=form)


@app.route("/register/")
@app.route("/register/", methods=["POST"])
def main_register():
    print(request.method)
    form = forms.register(request.form)
    print("fuera")
    if request.method == "POST":
        print("dentro")
        email = form.email.data
        name = form.name.data
        password = form.password.data
        surname = form.surname.data
        number = form.number.data
        companyType = form.companyType.data
        companyName = form.companyName.data
        cityHall = form.cityHall.data
        return auth.register(name, surname, number, email, password, companyType, companyName, cityHall)
    else:
        return render_template("register.html", form=form)


@app.route("/logout/")
def main_logout():
    auth.logout()
    return render_template("index.html")


# -------------------------------------Calendar-----------------------------------------------
@app.route("/calendar/")
@app.route("/calendar/", methods = ["POST,GET"])
def calendar():
    if "user_id" in session:
        user_id = session["user_id"]
        task = db.get_taks(str(user_id))
        current_day, current_month, current_year = GregorianCalendar.current_date()
        year = int(request.args.get("y", current_year))
        year = max(min(year, 9999), 1)
        month = int(request.args.get("m", current_month))
        month = max(min(month, 12), 1)
        month_name = GregorianCalendar.MONTH_NAMES[month - 1]
        weekdays_headers = ["LUN", "MAR", "MIE", "JUE", "VIE", "SAB", "DOM"]

        return cast(
            Response,
            render_template(
                "calendar.html",
                year=year,
                month=month,
                month_name=month_name,
                month_days=GregorianCalendar.month_days(year, month),
                previous_month_link=previous_month_link(year, month),
                next_month_link=next_month_link(year, month),
                weekdays_headers=weekdays_headers,
                tasks=task,
            ),
        )
    else:
        return redirect(url_for("index"))


def previous_month_link(year: int, month: int) -> str:
    month, year = GregorianCalendar.previous_month_and_year(year=year, month=month)
    return (
        ""
        if year < 1 or year > 9999
        else "?y={}&m={}".format(year, month)
    )


def next_month_link(year: int, month: int) -> str:
    month, year = GregorianCalendar.next_month_and_year(year=year, month=month)
    return (
        ""
        if year < 1 or year > 9999
        else "?y={}&m={}".format(year, month)
    )


# ----------------------------------Profile--------------------------------------------------
@app.route("/calendar/profile/")
def profile():
    if "user_id" in session:
        user_id = session["user_id"]
        user = db.get_user_profile(user_id)
        company = db.get_company_profile(user_id)
        companyTypeID = company[3]
        companyType = db.get_type_company_profile(companyTypeID)
        return render_template("profile.html", user=user, company=company, typeCompany=companyType)
    else:
        return redirect(url_for("index"))


# --------------------------------------Contacts----------------------------------------------
@app.route("/calendar/companies/")
def companies():
    if "user_id" in session:
        companyTipe = db.get_companies()
        return render_template("contact.html", companiesType=companyTipe)
    else:
        return redirect(url_for("index"))

@app.route("/calendar/companies/contact", methods=["POST"])
def contacts():
    if "user_id" in session:
        if request.method == "POST":
            companyID = request.form.get("companyID")
            print(companyID)
            companyTipe = db.get_companies()
            print(companyTipe)
            company = db.get_contacts()
            print(company)
            users = db.get_users()
            print(users)
            return render_template("contact.html", companiesType=companyTipe, company=company, users=users, companyID=int(companyID))
    else:
        return redirect(url_for("index"))
# ----------------------------------SEEDS---------------------------------------
@app.route("/calendar/seeds/")
def seeds():
    if "user_id" in session:
        seed = db.grow()
        return render_template("seeds.html", seeds=seed)
    else:
        return redirect(url_for("index"))


# ---------------------------------TASK--------------------------------------------
@app.route("/calendar/task/")
def tasks():
    if "user_id" in session:
        user = session["user_id"]
        notes = db.get_taks(user)
        return render_template("task.html", tasks=notes)
    else:
        return redirect(url_for("index"))

@app.route("/calendar/task/delete/")
@app.route("/calendar/task/delete/", methods=["POST"])
def tasks_delete():
    if "user_id" in session:
            print(request.method)
            user = session["user_id"]
            task = request.form.get("delete")
            print(task)
            db.delete_task(user, task)
            return redirect(url_for("tasks"))
    else:
        return redirect(url_for("index"))

@app.route("/calendar/task/create/")
@app.route("/calendar/task/create/", methods=["POST"])
def tasks_create():
    if "user_id" in session:
        form = forms.task(request.form)
        if request.method == "POST" and form.validate():
            user = session["user_id"]
            name = form.name.data
            comment = form.description.data
            date = form.date.data
            return db.set_task(user, name, comment, date)
        else:
            return render_template("createTask.html", form=form)
    else:
        return redirect(url_for("index"))


@app.route("/calendar/task/edit/")
@app.route("/calendar/task/edit/", methods=["POST"])
def tasks_edit():
    if "user_id" in session:
        print()
        if request.method == "POST" and request.form.get("nameTask"):
            user = session["user_id"]
            task = request.form.get("Enviar")
            name = request.form.get("nameTask")
            description = request.form.get("descriptionTask")
            date = request.form.get("dateTask")
            db.set_update_task(task, user, name, description, date)
            return redirect(url_for("tasks"))
        else:
            taskid = request.form.get("edit")
            print(taskid)
            task = db.get_update_task(taskid)
            return render_template("createTask.html", task=task)

    else:
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
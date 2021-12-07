# imports
import html
import flask

from flask import Flask, redirect, render_template, request, flash, url_for, current_app, abort
from datetime import datetime, date, time, timedelta
import calendar
import pymysql
from flask_login import login_required
from werkzeug.wrappers import Response
from typing import List, Optional, Tuple, cast  # noqa: F401

# own imports
import auth
import forms
import db
from gregorian_calendar import  GregorianCalendar
from  calendar_data import CalendarData
import constants

# definition of app
app = Flask(__name__)
# auth.LoginManager.init_app(app)

# connect DB
def conect():
    return pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="root",
                           db="calendariodb")

# secret key
app.secret_key = "VCGwYo8Kjr"


# ---------------------Global variables ---------------------


# paginas de errores
@app.errorhandler(404)
def page_no_found(e):
    return render_template("404.html")
# ------------------------------------------------------------------------------------
# rutas
@app.route("/")
def index():
    return render_template("index.html")

# ------------------------------------------------------------------------------------
# Login and registrer
@app.route("/login")
@app.route("/login", methods=["POST"])
def login():
    data = request.form
    form = forms.login(data)
    if request.method == "GET" and form.validate() == True:
            print(form.name.data)
            auth.login(form.email.data, form.name.data, form.password.data)
            flash("Ha iniciado correctamente")
            return redirect(url_for("calendar"))
    else:
        return render_template("login.html", form=form)


@app.route("/register")
@app.route("/register", methods=["POST,GET"])
def register():
    form = forms.register(request.form)
    if request.method == "POST" and form.validate():
        print(form.name.data)
        auth.register(form.name.data, form.surname.data,
                      form.number.data, form.email.data,
                      form.password.data, form.companyType.data,
                      form.cityHall.data, form.companyName.data)
        return redirect(url_for("calendar"))
    else:
        return render_template("register.html", form=form)

# ------------------------------------------------------------------------------------
# Calendar
@app.route("/calendario/")
# @login_required
def calendario() -> Response:
    current_day, current_month, current_year = GregorianCalendar.current_date()
    year = int(request.args.get("y", current_year))
    year = max(min(year, 9999), 1)
    month = int(request.args.get("m", current_month))
    month = max(min(month, 12), 1)
    month_name = GregorianCalendar.MONTH_NAMES[month - 1]

    weekdays_headers = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

    return cast(
        Response,
        render_template(
            "calendar.html",
            year=year,
            month=month,
            month_name=month_name,
            current_year=current_year,
            current_month=current_month,
            current_day=current_day,
            month_days=GregorianCalendar.month_days(year, month),
            previous_month_link=previous_month_link(year, month),
            next_month_link=next_month_link(year, month),

            weekdays_headers=weekdays_headers,
        ),
    )

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


# ------------------------------------------------------------------------------------

# Profile
@app.route("/calendario/profile")
def profile():
    return "algo"

# ------------------------------------------------------------------------------------

# Contactos
@app.route("/calendario/companies")
# @login_required
def companies():
    companies = db.companies()
    print(companies)
    return render_template("contacts.html", companies=companies)

@app.route("/calendario/companies/contacts")
@app.route("/calendario/companies/contacts", methods=["GET"])
# @login_required
def contacts():
    companies = db.companies()
    data = request.form.get("compañia")
    contacts = db.contacts(data)
    print(data)
    print(contacts)
    return render_template("contacts.html", companies=companies, contacts = contacts)


@app.route("/calendario/companies/contacts/contact")
@app.route("/calendario/companies/contacts/contact", methods=["POST,GET"])
# @login_required
def contact():
    companies = db.companies()
    contacts = db.contacts(request.form.values)
    print(contacts)
    contact = db.contact(request.form.values)
    print(contact)
    return render_template("contacts.html", companies=companies, contacts=contacts, contact=contact)


# -------------------------------------------------------------------------
# seeds
@app.route("/calendario/semillas")
# @login_required
def seeds():
    seed = db.grow()
    return render_template("seeds.html", seeds=seed)


# -----------------------------------------------------------------------------


# Taks
@app.route("/calendario/task")
# @login_required
def tasks():
    return render_template("task.html")




# Creation for debug
if __name__ == "__main__":
    app.run(debug=True)
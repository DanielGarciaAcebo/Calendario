# imports
import html
import flask

from flask import Flask, redirect, render_template, request, flash, url_for, current_app, abort
from datetime import datetime, date, time, timedelta
import calendar
import pymysql
import dayMonth
from flask_login import login_required
from werkzeug.wrappers import Response
from typing import List, Optional, Tuple, cast  # noqa: F401

# own imports
import auth
import forms
import db
import TraslateDate

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

SESSION_ID = "SessionId"

# Starts day, monday and Sunday
WEEK_START_DAY_MONDAY = 0
WEEK_START_DAY_SUNDAY = 6


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
def calendario():
    year = datetime.today().strftime("%Y")
    month = datetime.today().strftime("%m")
    mes = TraslateDate.month(month)
    day = datetime.today().strftime("%a")
    dia = TraslateDate.day(day)
    print(year, month, "-", mes, day, "-", dia)
    return render_template("calendar.html", mes=mes, year=year)

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
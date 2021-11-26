# imports
import flask
from flask import Flask, redirect, render_template, request, flash, url_for, current_app, abort
from datetime import datetime,date,timedelta
from flask_mysqldb import MySQL
from flask_login import login_required
import gregorian_calendar
from gregorian_calendar import  GregorianCalendar
from werkzeug.wrappers import Response
from typing import List, Optional, Tuple, cast  # noqa: F401

# own imports
import auth
import forms

# definition of app
app = Flask(__name__)
mysql = MySQL(app)
#auth.LoginManager.init_app(app)


# connect DB
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root "
app.config["MYSQL_DB"] = "Calendario"

# secret key
app.secret_key = "VCGwYo8Kjr"

#---------------------Global variables ---------------------

SESSION_ID = "sid"

# Starts day, monday and Sunday
WEEK_START_DAY_MONDAY = 0
WEEK_START_DAY_SUNDAY = 6

#---------------------Global variables ---------------------



# paginas de errores
@app.errorhandler(404)
def page_no_found(e):
    return render_template("404.html")


# context processors
@app.context_processor
def date_now():
    return {
        "now": datetime.utcnow()
    }


# rutas
@app.route("/")
def index():
    return render_template("index.html")

#Login and registrer
@app.route("/login")
@app.route("/login", methods=["POST,GET"])
def login():
    form = forms.login(request.form)
    if request.method == "POST" and form.validate():
         print(form.name.data)
         auth.login(form.mail.data, form.name.data, form.password.data)
         sentece = "Ha iniciado correctamente"
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
                      form.mail.data, form.password.data,
                      form.company.data, form.sector.data,
                      form.cityHall.data)
        sentece = "Se ha registrado correctamente"
        return redirect(url_for("calendar"))
    else:
        return render_template("register.html", form=form)


# Calendar

@app.route("/calendar")
# @login_required
def calendar(calendar_id: str) -> Response:
    GregorianCalendar.setfirstweekday(current_app.config["WEEK_STARTING_DAY"])

    current_day, current_month, current_year = GregorianCalendar.current_date()
    year = int(request.args.get("y", current_year))
    year = max(min(year, current_app.config["MAX_YEAR"]), current_app.config["MIN_YEAR"])
    month = int(request.args.get("m", current_month))
    month = max(min(month, 12), 1)
    month_name = GregorianCalendar.MONTH_NAMES[month - 1]

    if current_app.config["HIDE_PAST_TASKS"]:
        view_past_tasks = False
    else:
        view_past_tasks = request.cookies.get("ViewPastTasks", "1") == "1"

    # calendar_data = CalendarData(current_app.config["DATA_FOLDER"], current_app.config["WEEK_STARTING_DAY"])
    # try:
    #     data = calendar_data.load_calendar(calendar_id)
    # except FileNotFoundError:
    #     abort(404)

    if current_app.config["WEEK_STARTING_DAY"] == WEEK_START_DAY_MONDAY:
        weekdays_headers = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    else:
        weekdays_headers = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

    return cast(
        Response,
        render_template(
            "calendar.html",
            calendar_id=calendar_id,
            year=year,
            month=month,
            month_name=month_name,
            current_year=current_year,
            current_month=current_month,
            current_day=current_day,
            month_days=GregorianCalendar.month_days(year, month),
            previous_month_link=previous_month_link(year, month),
            next_month_link=next_month_link(year, month),
            base_url=current_app.config["BASE_URL"],
            display_view_past_button=current_app.config["SHOW_VIEW_PAST_BUTTON"],
            weekdays_headers=weekdays_headers,
        ),
    )

def previous_month_link(year: int, month: int) -> str:
    month, year = GregorianCalendar.previous_month_and_year(year=year, month=month)
    return (
        ""
        if year < current_app.config["MIN_YEAR"] or year > current_app.config["MAX_YEAR"]
        else "?y={}&m={}".format(year, month)
    )

def next_month_link(year: int, month: int) -> str:
    month, year = GregorianCalendar.next_month_and_year(year=year, month=month)
    return (
        ""
        if year < current_app.config["MIN_YEAR"] or year > current_app.config["MAX_YEAR"]
        else "?y={}&m={}".format(year, month)
    )

# Perfil
@app.route("/calendar/perfil")
# @login_required
def profile():
    return ""


# Contactos
@app.route("/calendar/contactos")
# @login_required
def contacts():
    return ""


# Contactos
@app.route("/calendar/grow")
# @login_required
def grow():
    return ""


# Creation for debug
if __name__ == "__main__":
    app.run(debug = True)


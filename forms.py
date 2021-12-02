# Imports
from flask_wtf import FlaskForm
from wtforms import Form
from wtforms import StringField, TextField, IntegerField, validators
from wtforms.fields.html5 import EmailField
from wtforms.fields import SelectField, DateField


# this classes are forms
# Forms of login and register

class login(Form):
    name = StringField("name",
                       [
                           validators.Required(message="Necesita poner un nombre"),
                           validators.length(min=4, max=25, message="Ingrese un nombre valido")
                       ])

    email = EmailField("email",
                       [
                           validators.Required(message="Necesita poner un correo electronico"),
                           validators.email(message="Ingrese un correo valido")
                       ])

    password = StringField("password",
                           [
                               validators.Required(message="Necesita poner una contraseña"),
                               validators.length(min=4, max=25,
                                                 message="Ingrese una contraseña con un maximo de 25 caracteres y un minimo de 4")
                           ])


class register(Form):
    name = StringField("name",
                       [
                           validators.Required(message="Necesita poner un nombre"),
                           validators.length(min=4, max=25, message="Ingrese un nombre valido")
                       ])

    surname = StringField("surname",
                          [
                              validators.Required(message="Necesita poner un nombre"),
                              validators.length(min=4, max=25, message="Ingrese apellidos validos")
                          ])
    number = IntegerField("number",
                          [
                              validators.Required(message="Necesita poner un numero"),
                              validators.length(min=9, max=9, message="Ingrese apellidos validos")
                          ])

    email = EmailField("email",
                       [
                           validators.Required(message="Necesita poner un correo electronico"),
                           validators.email(message="Ingrese un correo valido")
                       ])

    password = StringField("password",
                           [
                               validators.Required(message="Necesita poner una contraseña"),
                               validators.length(min=4, max=25,
                                                 message="Ingrese una contraseña con un maximo de 25 caracteres y un minimo de 4")
                           ])

    company = SelectField("company", choices=[("1", "ganadero"),
                                              ("2", "agricultor"),
                                              ("3", "Com maquinaria"),
                                              ("4", "veterinario")])

    companyName = StringField("companyName",
                           [
                               validators.Required(message="Necesita poner un nomnbre de tu compañia"),
                               validators.length(min=4, max=30,
                                                 message="El nombre no puede tener mas de 25 caracteres")
                           ])

    cityHall = StringField("cityHall",
                           [
                               validators.Required(message="Necesita poner un ayuntamiento"),
                               validators.length(min=4, max=25, message="Ingrese un ayuntamiento valido")
                           ])


# form of task
class task(Form):
    name = StringField("name",
                       [
                           validators.Required(message="Tiene que poner un nombre"),
                           validators.length(min=1, max=15, message="Ingrese un nombre valido entre 1 y 15")
                       ])

    description = TextField("Description",
                            [
                                validators.length(max=100, message="no puede ingresar mas de 100 caracteres")
                            ])

    date = DateField("Date",
                     [
                         validators.Required(message="Es obligatorio introducir una fecha")
                     ])

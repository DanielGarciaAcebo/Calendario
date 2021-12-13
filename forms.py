# Imports
from flask_wtf import FlaskForm
import wtforms
from wtforms import Form
from wtforms import StringField, IntegerField, validators, EmailField, PasswordField, TextAreaField
from wtforms.fields import SelectField, DateField
from wtforms.validators import DataRequired

# this classes are forms
# Forms of login and register
import db


class login(Form):
    name = StringField("Nombre",
                       [
                           DataRequired(message="Necesita poner un nombre"),
                           validators.length(min=1, max=25, message="Ingrese un nombre valido")
                       ])

    email = EmailField("Email",
                       [
                           DataRequired(message="Necesita poner un correo electronico"),
                           validators.email(message="Ingrese un correo valido")
                       ])

    password = PasswordField("Contraseña",
                             [
                                 DataRequired(message="Necesita poner una contraseña"),
                                 validators.length(min=4, max=25,
                                                   message="Ingrese una contraseña con un maximo de 25 caracteres y un minimo de 4")
                             ])


class register(Form):
    name = StringField("Nombre",
                       [
                           DataRequired(message="Necesita poner un nombre"),
                           validators.Length(min=1, max=25, message="Ingrese un nombre valido")
                       ])

    surname = StringField("Apellido",
                          [
                              DataRequired(message="Necesita poner un apellido"),
                              validators.Length(min=1, max=25, message="Ingrese un apellido valido")

                          ])

    email = EmailField("Email",
                       [
                           DataRequired(message="Necesita poner un correo electronico"),
                           validators.email(message="Ingrese un correo valido")

                       ])

    number = IntegerField("Telefono",
                          [
                              DataRequired(message="Necesita poner un telefono"),
                              validators.Length(min=8, max=10,
                                                message="Ingrese un numero valido")
                          ])

    password = PasswordField("Contraseña",
                             [
                                 DataRequired(message="Necesita poner una contraseña"),
                                 validators.Length(min=4, max=25,
                                                   message="Ingrese una contraseña con un maximo de 25 caracteres y un minimo de 4")
                             ])

    companyType = SelectField("Trabajo", default=1, choices=[("1", "Ganadero"),
                                                             ("2", "Agricultor"),
                                                             ("3", "Maquinista"),
                                                             ("4", "Veterinario")]
                              )

    companyName = StringField("Compañia",
                              [
                                  DataRequired(message="Necesita poner un nomnbre de tu compañia"),
                                  validators.Length(min=4, max=100,
                                                    message="El nombre no puede tener mas de 25 caracteres")
                              ])

    cityHall = StringField("Ayuntamiento",
                           [
                               DataRequired(message="Necesita poner un ayuntamiento"),
                               validators.Length(min=4, max=100, message="Ingrese un ayuntamiento valido")
                           ])


# form of task
class task(Form):
    name = StringField("Nombre",
                       [
                           DataRequired(message="Tiene que poner un nombre"),
                           validators.Length(min=1, max=15, message="Ingrese un nombre valido entre 1 y 15")
                       ])

    description = TextAreaField("Descripcion",
                                [
                                    validators.Length(max=200, message="no puede ingresar mas de 100 caracteres")
                                ])

    date = DateField("Fecha",
                     [
                         DataRequired(message="Es obligatorio introducir una fecha")
                     ])

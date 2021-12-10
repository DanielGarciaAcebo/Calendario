# Imports
from flask_wtf import FlaskForm
import wtforms
from wtforms import Form
from wtforms import StringField, IntegerField, validators, EmailField, PasswordField
from wtforms.fields import SelectField, DateField
from wtforms.validators import DataRequired


# this classes are forms
# Forms of login and register

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
    name = StringField("Name",
                       [
                           DataRequired(message="Necesita poner un nombre"),
                           validators.length(min=1, max=25, message="Ingrese un nombre valido")
                       ])

    surname = StringField("Apellidos",
                          [
                              DataRequired(message="Necesita poner un nombre"),
                              validators.length(min=1, max=25, message="Ingrese apellidos validos")
                          ])
    number = IntegerField("Numero de telefono",
                          [
                              DataRequired(message="Necesita poner un numero"),
                              validators.length(min=9, max=9, message="Ingrese apellidos validos")
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

    companyType = SelectField("Tipo de Compañia", choices=[("1", "ganadero"),
                                              ("2", "agricultor"),
                                              ("3", "Com maquinaria"),
                                              ("4", "veterinario")])

    companyName = StringField("Nombre de la compañia",
                           [
                               DataRequired(message="Necesita poner un nomnbre de tu compañia"),
                               validators.length(min=4, max=30,
                                                 message="El nombre no puede tener mas de 25 caracteres")
                           ])

    cityHall = StringField("Ayuntamiento",
                           [
                               DataRequired(message="Necesita poner un ayuntamiento"),
                               validators.length(min=4, max=25, message="Ingrese un ayuntamiento valido")
                           ])


# form of task
class task(Form):
    name = StringField("Nombre",
                       [
                           DataRequired(message="Tiene que poner un nombre"),
                           validators.length(min=1, max=15, message="Ingrese un nombre valido entre 1 y 15")
                       ])

    description = StringField("Descripcion",
                            [
                                validators.length(max=200, message="no puede ingresar mas de 100 caracteres")
                            ])

    date = DateField("Fecha",
                     [
                         DataRequired(message="Es obligatorio introducir una fecha")
                     ])

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


# Formular für die Registrierung
class RegisterForm(FlaskForm):
    username = StringField("Benutzername", validators=[DataRequired(), Length(min=3, max=80)])
    email = StringField("E-Mail", validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField("Passwort", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField(
        "Passwort wiederholen",
        validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Registrieren")


# Formular für den Login
class LoginForm(FlaskForm):
    email = StringField("E-Mail", validators=[DataRequired(), Email()])
    password = PasswordField("Passwort", validators=[DataRequired()])
    submit = SubmitField("Einloggen")

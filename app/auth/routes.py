from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy import or_

from . import auth_bp
from .forms import RegisterForm, LoginForm
from app.extensions import db
from app.models import User


# Route für die Registrierung
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    # Bereits eingeloggte Nutzer zum Dashboard weiterleiten
    if current_user.is_authenticated:
        return redirect(url_for("tasks.dashboard"))

    form = RegisterForm()

    if form.validate_on_submit():
        # Prüft, ob Benutzername oder E-Mail schon existieren
        existing_user = User.query.filter(
            or_(
                User.username == form.username.data,
                User.email == form.email.data
            )
        ).first()

        if existing_user:
            flash("Benutzername oder E-Mail existiert bereits.", "danger")
            return redirect(url_for("auth.register"))

        # Neuen Benutzer anlegen
        user = User(
            username=form.username.data,
            email=form.email.data
        )
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash("Registrierung erfolgreich. Du kannst dich jetzt einloggen.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", form=form)


# Route für den Login
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    # Bereits eingeloggte Nutzer zum Dashboard weiterleiten
    if current_user.is_authenticated:
        return redirect(url_for("tasks.dashboard"))

    form = LoginForm()

    if form.validate_on_submit():
        # Benutzer per E-Mail suchen
        user = User.query.filter_by(email=form.email.data).first()

        # Passwort prüfen und einloggen
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Erfolgreich eingeloggt.", "success")
            return redirect(url_for("tasks.dashboard"))

        flash("Ungültige E-Mail oder Passwort.", "danger")

    return render_template("auth/login.html", form=form)


# Route für den Logout
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Du wurdest ausgeloggt.", "info")
    return redirect(url_for("auth.login"))

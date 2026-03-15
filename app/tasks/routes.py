from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from sqlalchemy import case

from . import tasks_bp
from .forms import TaskForm
from app.extensions import db
from app.models import Task


# Dashboard mit Formular und Aufgabenliste
@tasks_bp.route("/", methods=["GET", "POST"])
@login_required
def dashboard():
    form = TaskForm()

    # Neue Aufgabe speichern
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            priority=form.priority.data,
            user_id=current_user.id
        )
        db.session.add(task)
        db.session.commit()
        flash("Aufgabe wurde erstellt.", "success")
        return redirect(url_for("tasks.dashboard"))

    # Reihenfolge der Prioritäten festlegen
    priority_order = case(
        (Task.priority == "hoch", 1),
        (Task.priority == "mittel", 2),
        (Task.priority == "niedrig", 3),
        else_=4
    )

    # Aufgaben des aktuellen Benutzers sortiert laden
    tasks = Task.query.filter_by(user_id=current_user.id).order_by(
        Task.is_done.asc(),
        priority_order.asc(),
        Task.created_at.desc()
    ).all()

    return render_template("tasks/dashboard.html", form=form, tasks=tasks)


# Aufgabe als erledigt/offen umschalten
@tasks_bp.route("/<int:task_id>/toggle", methods=["POST"])
@login_required
def toggle_task(task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    task.is_done = not task.is_done
    db.session.commit()

    flash("Aufgabe aktualisiert.", "info")
    return redirect(url_for("tasks.dashboard"))


# Aufgabe löschen
@tasks_bp.route("/<int:task_id>/delete", methods=["POST"])
@login_required
def delete_task(task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    db.session.delete(task)
    db.session.commit()

    flash("Aufgabe gelöscht.", "warning")
    return redirect(url_for("tasks.dashboard"))

from datetime import datetime
from app.extensions import db


# Datenbankmodell für eine Aufgabe
class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)  # Eindeutige ID der Aufgabe
    title = db.Column(db.String(150), nullable=False)  # Titel der Aufgabe
    priority = db.Column(db.String(20), nullable=False, default="mittel")  # Priorität
    is_done = db.Column(db.Boolean, nullable=False, default=False)  # Erledigt-Status
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Erstellungszeitpunkt

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)  # Zugehöriger Benutzer

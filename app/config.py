import os
from dotenv import load_dotenv

# Lädt Umgebungsvariablen aus einer .env-Datei,
# damit sensible Daten wie Schlüssel oder Datenbank-URLs
# nicht direkt im Code stehen müssen
load_dotenv()

class Config:
    # Geheimer Schlüssel für Flask, z. B. für Sessions und CSRF-Schutz.
    # Falls keine Umgebungsvariable gesetzt ist, wird ein Standardwert verwendet.
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")

    # Verbindungsadresse zur Datenbank.
    # Zuerst wird versucht, den Wert aus der Umgebungsvariable DATABASE_URL zu laden.
    # Falls diese nicht existiert, wird die lokale PostgreSQL-Datenbank verwendet.
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres123@localhost:5432/taskdb"
    )

    # Deaktiviert die Änderungsverfolgung von SQLAlchemy,
    # da sie zusätzlichen Speicher verbraucht und meist nicht benötigt wird.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

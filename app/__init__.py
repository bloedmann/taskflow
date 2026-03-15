from flask import Flask, redirect, url_for
from flask_login import current_user
from .config import Config
from .extensions import db, login_manager


def create_app():
    # Erstellt die Flask-Anwendung
    app = Flask(__name__)
    
    # Lädt die Konfiguration aus der Config-Klasse
    app.config.from_object(Config)

    # Initialisiert die Datenbank mit der App
    db.init_app(app)
    
    # Initialisiert den Login-Manager mit der App
    login_manager.init_app(app)

    # Importiert die Modelle, damit sie der App bekannt sind
    from .models import User, Task

    @login_manager.user_loader
    def load_user(user_id):
        # Lädt einen Benutzer anhand seiner ID
        return User.query.get(int(user_id))

    # Importiert die Blueprints für Authentifizierung, Tasks und API
    from .auth import auth_bp
    from .tasks import tasks_bp
    from .api import api_bp

    # Registriert die Blueprints in der Anwendung
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(api_bp)

    @app.route("/")
    def index():
        # Startseite:
        # Wenn der Benutzer eingeloggt ist, weiter zum Dashboard
        if current_user.is_authenticated:
            return redirect(url_for("tasks.dashboard"))
        
        # Andernfalls zur Login-Seite weiterleiten
        return redirect(url_for("auth.login"))

    # Gibt die fertig konfigurierte App zurück
    return app

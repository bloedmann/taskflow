from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Erstellt die SQLAlchemy-Instanz für die Datenbankanbindung.
# Sie wird später in der App mit app.init_app(...) verknüpft.
db = SQLAlchemy()

# Erstellt den Login-Manager für die Benutzer-Authentifizierung.
# Er verwaltet Login-Status, Benutzer-Sessions und geschützte Bereiche.
login_manager = LoginManager()

# Gibt an, auf welche Route nicht eingeloggte Benutzer
# weitergeleitet werden, wenn sie eine geschützte Seite aufrufen.
login_manager.login_view = "auth.login"

# Nachricht, die angezeigt wird, wenn ein Benutzer zuerst
# eingeloggt sein muss, um auf eine geschützte Seite zuzugreifen.
login_manager.login_message = "Bitte zuerst einloggen."

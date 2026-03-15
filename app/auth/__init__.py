from flask import Blueprint

# Auth-Blueprint mit Präfix /auth
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# Importiert die zugehörigen Routen
from . import routes

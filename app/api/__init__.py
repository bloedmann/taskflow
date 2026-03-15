from flask import Blueprint

# API-Blueprint mit Präfix /api
api_bp = Blueprint("api", __name__, url_prefix="/api")

# Importiert die zugehörigen Routen
from . import routes

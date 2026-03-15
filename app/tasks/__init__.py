from flask import Blueprint

# Tasks-Blueprint mit Präfix /tasks
tasks_bp = Blueprint("tasks", __name__, url_prefix="/tasks")

# Importiert die zugehörigen Routen
from . import routes

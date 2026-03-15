from flask import jsonify, request, Response

from . import api_bp
from app.models import User, Task


def unauthorized():
    return Response(
        response='{"error":"Authentifizierung erforderlich"}',
        status=401,
        mimetype="application/json",
        headers={"WWW-Authenticate": 'Basic realm="Taskflow API"'}
    )


def get_api_user():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return None

    user = User.query.filter_by(email=auth.username).first()

    if user and user.check_password(auth.password):
        return user

    return None


def task_to_dict(task):
    return {
        "id": task.id,
        "title": task.title,
        "priority": task.priority,
        "is_done": task.is_done,
        "created_at": task.created_at.isoformat() if task.created_at else None,
        "user_id": task.user_id,
    }


@api_bp.route("/tasks", methods=["GET"])
def get_tasks():
    user = get_api_user()
    if not user:
        return unauthorized()

    tasks = Task.query.filter_by(user_id=user.id).all()

    return jsonify({
        "tasks": [task_to_dict(task) for task in tasks],
        "count": len(tasks)
    })


@api_bp.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    user = get_api_user()
    if not user:
        return unauthorized()

    task = Task.query.filter_by(id=task_id, user_id=user.id).first()

    if not task:
        return jsonify({"error": "Task nicht gefunden"}), 404

    return jsonify(task_to_dict(task))
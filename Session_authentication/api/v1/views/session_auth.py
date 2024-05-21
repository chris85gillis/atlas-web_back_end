#!/usr/bin/env python3
"""Flask view that handles authentication sessions."""
from flask import jsonify, request, make_response, abort
from api.v1.views import app_views
from models.user import User
from api.v1.app import auth
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """Logs in a user using session authentication."""
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400
    pwd = request.form.get('password')
    if not pwd:
        return jsonify({"error": "password missing"}), 400
    user_list = User.search({'email': email})
    if not user_list:
        return jsonify({"error": "no user found for this email"}), 404
    user = user_list[0]
    if not user.is_valid_password(pwd):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)

    response = make_response(jsonify(user.to_json()))
    response.set_cookie(os.getenv('SESSION_NAME'), session_id)

    return response


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """Logs out a user using session authentication."""
    if not auth.destroy_session(request):
        abort(404)
    else:
        return jsonify(), 200

#!/usr/bin/env python3
"""Flask app"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound
from utils import _generate_uuid


app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def hello():
    """A route decorator that handles the root URL ("/")
    and returns a JSON response with a welcome message."""
    return jsonify(message="Bienvenue")


@app.route('/users', methods=['POST'])
def register_user():
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """
    Endpoint to log in a user.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie('session_id', session_id)
    return response


@app.route('/sessions', methods=['DELETE'])
def logout():
    """
    Endpoint to log out a user.
    """
    session_id = request.cookies.get('session_id')
    if not session_id:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=['GET'])
def profile():
    """
    Endpoint to get the user profile.
    """
    session_id = request.cookies.get('session_id')
    if not session_id:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token(self, email: str) -> str:
    """
     Get a reset password token for the user with the given email.
    """
    try:
        user = self._db.find_user_by(email=email)
    except NoResultFound:
        raise ValueError("User does not exist")
    reset_token = _generate_uuid()
    self._db.update_user(user.id, reset_token=reset_token)
    return reset_token


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

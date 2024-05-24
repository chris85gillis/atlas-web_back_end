#!/usr/bin/env python3
"""Flask app"""
from flask import Flask, jsonify, request
from auth import Auth

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

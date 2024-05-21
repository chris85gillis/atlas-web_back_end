#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from flask import Blueprint
from api.v1.views.users import User, session_auth

# Create a Blueprint instance for the views
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *

# Load users from file
User.load_from_file()

# Register the session_auth blueprint
app_views.register_blueprint(session_auth.app_views)

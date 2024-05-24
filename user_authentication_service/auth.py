#!/usr/bin/env python3
"""
Module handling password hashing using the bycrypt library.
"""
import bcrypt
from db import DB
from user import User
from auth import _hash_password

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user."""
        existing_user = self._db.find_user_by(email=email)
        if existing_user:
            raise ValueError(f"User {email} already exists")
        
        hashed_password = _hash_password(password)
        new_user = self._db.add_user(email, hashed_password)
        return new_user

def _hash_password(password: str) -> bytes:
    '''Hashes password'''
    byte_repr = password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=15)
    return bcrypt.hashpw(byte_repr, salt)

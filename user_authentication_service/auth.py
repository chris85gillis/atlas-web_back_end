#!/usr/bin/env python3
"""
Module handling password hashing using the bycrypt library.
"""
import bcrypt
from db import DB
from user import User
from auth import _hash_password
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register user"""
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            passwd = _hash_password(password)
            new_usr = self._db.add_user(email, passwd)
            return new_usr


def _hash_password(password: str) -> bytes:
    """Hashes password"""
    byte_repr = password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=15)
    return bcrypt.hashpw(byte_repr, salt)
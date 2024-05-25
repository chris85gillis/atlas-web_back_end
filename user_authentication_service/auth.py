#!/usr/bin/env python3
"""
Module handling password hashing using the bycrypt library.
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """Hashes password"""
    byte_repr = password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=15)
    return bcrypt.hashpw(byte_repr, salt)


def _generate_uuid() -> str:
    """Generate a new UUID."""
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """Validate login credentials."""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a session for the user."""
        user = self._db.find_user_by(email=email)
        if user:
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        Retrieve a user based on a session ID.
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Destroy the session for a given user ID.
        """
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
        except NoResultFound:
            pass

    def get_reset_password_token(self, email: str) -> str:
        '''Generate reset password token'''
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError("User does not exist")
        if user is not None:
            reset_token = str(uuid.uuid4())
            user.reset_token = reset_token
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token

#!/usr/bin/env python3
"""
Module handling password hashing using the bycrypt library.
"""
import bycrypt


def hash_password(password: str) -> bytes:
    """hashes the input password"""
    salt = bycrypt.gensalt()
    hased_password = bycrypt.hashpw(password.encode(), salt)
    return hased_password

#!/usr/bin/env python3
"""
class for all authentications
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """public mehtods for authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if auth is required, returning a boolean"""
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        for excl_path in excluded_paths:
            if path.rstrip('/') == excl_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns the authorization header from a request as a string"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current user based on the request as a TypeVar"""
        return None

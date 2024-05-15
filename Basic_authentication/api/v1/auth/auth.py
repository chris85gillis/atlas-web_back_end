#!/usr/bin/env python3
"""
class for all authentications
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """public mehtods for authentication"""
    def authorization_header(self, request=None) -> str:
        """Returns the Authorization header value from the request"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def authorization_header(self, request=None) -> str:
        """Returns the value of the Authorization
        header if present, otherwise None"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current user based on the request as a TypeVar"""
        return None

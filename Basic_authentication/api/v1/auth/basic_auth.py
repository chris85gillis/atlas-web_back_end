#!/usr/bin/env python3
"""
class for basic authentications
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """class for BasicAuth"""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        A function to extract the base64 part from the authorization header.
        """
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ")[1] if len(authorization_header.split(" ")) == 2 else None

#!/usr/bin/env python3
"""
class for basic authentications
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """class for BasicAuth"""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        # Split the header and extract the base64 part
        return authorization_header.split(" ")[1] if len(authorization_header.split(" ")) == 2 else None

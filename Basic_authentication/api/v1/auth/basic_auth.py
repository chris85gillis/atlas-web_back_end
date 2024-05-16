#!/usr/bin/env python3
"""
class for basic authentications
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """class for BasicAuth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        A function to extract the base64 part from the authorization header.
        """
        if authorization_header is None or \
                not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ")[1] \
            if len(authorization_header.split(" ")) == 2 else None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes the base64 authorization header and return the decoded string.
        """
        if base64_authorization_header is None or \
                not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except:
            return None

#!/usr/bin/env python3
"""Basic authentication: class that inherits from auth class"""
from typing import tuple
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Inherits properties of class Auth"""

    def extract_base64_authorization_header(self, authorization_header:
                                            str) -> str:
        """Returns base64 of authorization header"""
        if (authorization_header is None or
                type(authorization_header) is not str or
                authorization_header.split(" ")[0] != 'Basic'):
            return None
        else:
            return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """Basic - Base64 decode"""
        if (base64_authorization_header is None or
                type(base64_authorization_header) is not str):
            return None
        try:
            return (base64.b64decode(base64_authorization_header)
                    .decode('utf-8'))
            except Exception:
                return None

    def extract_user_credentials(
                                 self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """Returns username and password from base64"""
        if (decoded_base64_authorization_header is None
                or type(decoded_base64_authorization_header) is not str
                or ":" not in decoded_base64_authorization_header):
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(":", 1))

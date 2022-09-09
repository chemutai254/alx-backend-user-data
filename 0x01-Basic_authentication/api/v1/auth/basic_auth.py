#!/usr/bin/env python3
"""Basic authentication: class that inherits from auth class"""

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

#!/usr/bin/env python3
"""Function that returns the log message obfuscated"""


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str):
    """
    Function uses regex to replace occurrences of of certain field values
    """
    for item in fields:
        message = re.sub(item + '=.*?' + separator, item + '=' +
                         redaction + separator, message)
        return message

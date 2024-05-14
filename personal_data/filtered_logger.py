#!/usr/bin/env python3
"""Filtered Logger"""
import re
import logging
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
        ) -> str:
    '''Returns the log message obfuscated'''
    pattern = '|'.join(re.escape(field) for field in fields)
    return re.sub(f'({pattern})=(.*?){re.escape(separator)}',
                  f'\\1={redaction}{separator}', message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initializes a RedactingFormatter object."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """A description of the entire function, its parameters, and its return types."""
        message = filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)
        return self._fmt % record.__dict__ + message

#!/usr/bin/env python3
"""Filtered Logger"""
import re
import logging
import mysql.connector
import os
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
        """Filter values in incoming log records"""
        message = record.msg
        for field in self.fields:
            message = filter_datum([field], self.REDACTION,
                                   message, self.SEPARATOR)
        record.msg = message
        return super().format(record)


PII_FIELDS = (
    "name",
    "email",
    "phone",
    "ssn",
    "password",
)
DATA_FILE = "user_data.csv"


def get_logger() -> logging.Logger:
    """Returns a logger object for user_data"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Returns a connection to the database"""
    db_username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    if not db_name:
        raise ValueError("Database name is not set")

    db = mysql.connector.connect(
        user=db_username,
        password=db_password,
        host=db_host,
        database=db_name
    )
    return db

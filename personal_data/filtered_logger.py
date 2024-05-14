#!/usr/bin/env python3
"""Filtered Logger"""
import re


def filter_datum(fields, redaction, message, separator):
    """Using re.sub to replace field values with redaction"""
    return re.sub(r'(?<=\b|\s|^)(' + '|'.join(fields) + r')=[^;]*', r'\1=' + redaction, message)

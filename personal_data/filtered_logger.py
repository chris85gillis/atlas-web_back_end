#!/usr/bin/env python3
import re


def filter_datum(fields, redaction, message, separator):
    return re.sub(r'(?<=\b|\s|^)(' + '|'.join(fields) + r')=[^;]*', r'\1=' + redaction, message)

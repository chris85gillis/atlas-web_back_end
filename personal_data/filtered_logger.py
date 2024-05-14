#!/usr/bin/env python3
"""Filtered Logger"""
import re


def filter_datum(fields, redaction, message, separator):
    '''Returns the log message obfuscated'''
    return re.sub(r'(?<=\b|\s|^)(' + '|'.join(fields) + r')=[^;]*', r'\1=' + redaction, message)

# -*- coding: utf-8 -*-
                

import re


class NdbValidationError(Exception):
    pass


def length(min=None, max=None):
    """
    Length validator.
    The string must have a minimal length of min and maximal length of max characters.
    
    :param min: Minimum length
    :param max: Maximal length
    :type min: int
    :type max: int
    """
    def length_validator(prop, value):
        if min and len(value) < min:
            raise NdbValidationError('{} must be greater than {} characters'.format(prop, min))
        if max and len(value) > max:
            raise NdbValidationError('{} must be less than {} characters'.format(prop, max))
        return None
    return length_validator


def regexp(regex, flags=0):
    """
    Regular expression validator.
    String must match given regex.

    :param regex: The regular expression string to use.
    :param flags: The regex flags to use, e.g. re.IGNORECASE.
    :type regex: str
    :type flags: int
    """
    def regex_validator(prop, value):
        if not re.match(regex, value, flags=flags):
            raise NdbValidationError('Invaild input')
        return None
    return regex_validator

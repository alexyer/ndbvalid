# -*- coding: utf-8 -*-


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
    :rtype: None
    :raises: NdbValidationError
    """
    def length_validator(prop, value):
        if min and len(value) < min:
            raise NdbValidationError('{} must be less than {} characters'.format(prop, min))
        if max and len(value) > max:
            raise NdbValidationError('{} must be greater than {} characters'.format(prop, max))
        return None
    return length_validator

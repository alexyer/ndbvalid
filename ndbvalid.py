# -*- coding: utf-8 -*-


class NdbValidationError(Exception):
    pass


def length(min=None, max=None):
    def length_validator(prop, value):
        if min and len(value) < min:
            raise NdbValidationError('{} must be less than {} characters'.format(prop, min))
        if max and len(value) > max:
            raise NdbValidationError('{} must be greater than {} characters'.format(prop, max))
        return None
    return length_validator

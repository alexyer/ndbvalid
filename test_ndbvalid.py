# -*- coding: utf-8 -*-


from unittest import TestCase
import ndbvalid
import re


class TestValidators(TestCase):

    def test_length_validator(self):
        validator = ndbvalid.length(min=7, max=15)

        with self.assertRaises(ndbvalid.NdbValidationError):
            validator({}, 'short')

        with self.assertRaises(ndbvalid.NdbValidationError):
            validator({}, 'too loooooong string')

        self.assertIsNone(validator({}, 'normal string'))

    def test_regex_validator(self):
        validator = ndbvalid.regexp(r'[a-z]+')

        with self.assertRaises(ndbvalid.NdbValidationError):
            validator({}, '1')

        with self.assertRaises(ndbvalid.NdbValidationError):
            validator({}, 'Invalid')

        self.assertIsNone(validator({}, 'valid'))

        validator = ndbvalid.regexp(r'[a-z]+', re.IGNORECASE)

        with self.assertRaises(ndbvalid.NdbValidationError):
            validator({}, '1')

        self.assertIsNone(validator({}, 'Valid'))

# -*- coding: utf-8 -*-


from unittest import TestCase
import ndbvalid


class TestValidators(TestCase):

    def test_length_validator(self):
        validator = ndbvalid.length(min=7, max=15)

        with self.assertRaises(ndbvalid.NdbValidationError):
            validator({}, 'short')

        with self.assertRaises(ndbvalid.NdbValidationError):
            validator({}, 'too loooooong string')

        self.assertIsNone(validator({}, 'normal string'))

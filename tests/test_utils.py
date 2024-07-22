import unittest

from utils.conversions import parse_int
from utils.response import dict_response


class TestConversions(unittest.TestCase):
    def test_parse_int_valid(self):
        expected = 5
        actual = parse_int('5')
        self.assertEqual(expected, actual)

    def test_parse_int_valid_default(self):
        expected = 5
        actual = parse_int('5', 240)
        self.assertEqual(expected, actual)

    def test_parse_int_invalid(self):
        actual = parse_int('5a')
        self.assertIsNone(actual)

    def test_parse_int_invalid_default(self):
        expected = 7
        actual = parse_int('5a', 7)
        self.assertEqual(expected, actual)

    def test_parse_int_none(self):
        actual = parse_int(None)
        self.assertIsNone(actual)

    def test_parse_int_none_default(self):
        expected = 20
        actual = parse_int(None, 20)
        self.assertEqual(actual, expected)


class TestResponse(unittest.TestCase):
    def test_dict_response(self):
        actual = dict_response({
            'something': 4,
            'else': 9,
            'yes': 'ofcourse'
        })

        self.assertEqual('application/json', actual.mimetype)
        self.assertEqual(b'{"something": 4, "else": 9, "yes": "ofcourse"}', actual.data)

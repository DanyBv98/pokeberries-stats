import unittest

from models.berries import Berry


class TestBerries(unittest.TestCase):
    def test_dict_parsing(self):
        data = {
            'name': 'someberry',
            'growth_time': 10
        }
        
        expected = Berry(name='someberry', growth_time=10)
        actual = Berry.from_dict(data)

        self.assertEqual(expected, actual)

    def test_invalid_berry_parsing(self):
        data = {
            'namez': 'someberry',
            'growth_time': 10
        }
        
        actual = Berry.from_dict(data)

        self.assertIsNone(actual)
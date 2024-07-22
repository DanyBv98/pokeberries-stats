import json
import unittest
from unittest import mock

from app import app
from models.berries import Berry


class TestClientMixin:
    client = app.test_client()

class TestAllBerryStats(TestClientMixin, unittest.TestCase):
    @mock.patch('app.get_berries', new_callable=mock.AsyncMock)
    def test_get_all_berry_stats(self, get_berries_mock):
        get_berries_mock.return_value = [
            Berry(name='berryone', growth_time=5),
            Berry(name='secondberry', growth_time=2),
            Berry(name='thatberry', growth_time=5),
            Berry(name='noberry', growth_time=20),
        ]

        expected = json.dumps({
            'berries_names': ['berryone', 'secondberry', 'thatberry', 'noberry'],
            'min_growth_time': 2,
            'median_growth_time': 5.0,
            'max_growth_time': 20,
            'variance_growth_time': 49.5,
            'mean_growth_time': 8.0,
            'frequency_growth_time': {5: 2, 2: 1, 20: 1}
        })
        actual = self.client.get('/allBerryStats')

        self.maxDiff = None
        self.assertEqual(expected, actual.data.decode('utf-8'))
        self.assertEqual('application/json', actual.mimetype)

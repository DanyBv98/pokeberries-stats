import unittest
from unittest import mock

from api.berries import get_berries
from caching.cache import redis_instance
from models.berries import Berry

class RedisTestMixin:
    def setUp(self):
        redis_instance.flushdb()
        super().setUp()

class TestFetchBerries(RedisTestMixin, unittest.IsolatedAsyncioTestCase):
    @mock.patch('api.berries.fetch_multiple_json', new_callable=mock.AsyncMock)
    @mock.patch('api.berries.__fetch_berries_urls', new_callable=mock.AsyncMock)
    async def test_get_berries(self, fetch_urls_mock: mock.AsyncMock, fetch_all_beries_mock: mock.AsyncMock):
        fetch_urls_mock.return_value = ['url1', 'url2', 'url3']
        fetch_all_beries_mock.return_value = [
            {'name': 'someberry', 'growth_time': 5},
            {'namezz': 'somethingelse'},
            {'name': 'otherberry', 'growth_time': 7},
        ]

        actual = await get_berries()
        expected = [
            Berry(name='someberry', growth_time=5),
            Berry(name='otherberry', growth_time=7),
        ]

        fetch_all_beries_mock.assert_called_once_with(['url1', 'url2', 'url3'])
        self.assertEqual(expected, actual)

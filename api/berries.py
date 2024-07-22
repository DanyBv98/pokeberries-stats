from redis.lock import Lock

from api.fetch import fetch_multiple_json, fetch_paginated_json
from api.urls import ExternalUrls
from caching.cache import redis_instance
from caching.serialization import deserialize, serialize
from constants.redis import RedisKeys
from models.berries import Berry
from settings import app_settings


async def __fetch_berries_urls() -> list[str]:
    results = await fetch_paginated_json(ExternalUrls.berries())
    return [berry['url'] for berry in results]

async def get_berries() -> list[Berry]:
    with Lock(redis_instance, RedisKeys.BERRIES_LOCK, timeout=app_settings.BERRIES_LOCK_TIMEOUT):
        # locking to prevent multiple requests from creating at the same time

        berries_bytes = redis_instance.get(RedisKeys.BERRIES)
        if not berries_bytes:
            berries_urls = await __fetch_berries_urls()
            berries_data = await fetch_multiple_json(berries_urls)
            berries = [Berry.from_dict(item) for item in berries_data]
            redis_instance.set(RedisKeys.BERRIES, serialize(berries), ex=app_settings.BERRIES_CACHE_TTL)
        else:
            berries = deserialize(berries_bytes)
        return berries

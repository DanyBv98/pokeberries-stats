import redis

from settings import app_settings


redis_instance = redis.Redis.from_url(app_settings.REDIS_URL)

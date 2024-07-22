from dotenv import dotenv_values

from utils.conversions import parse_int


class Settings:
    @property
    def EXTERNAL_API_ROOT(self):
        return self.__EXTERNAL_API_ROOT
    
    @property
    def BERRIES_CACHE_TTL(self):
        return self.__BERRIES_CACHE_TTL
    
    @property
    def BERRIES_LOCK_TIMEOUT(self):
        return self.__BERRIES_LOCK_TIMEOUT

    @property
    def REDIS_URL(self):
        return self.__REDIS_URL

    def __init__(self, config: dict[str, str | None]) -> None:
        self.__EXTERNAL_API_ROOT = config.get('API_ROOT', 'https://pokeapi.co/api/v2')
        self.__BERRIES_CACHE_TTL = parse_int(config.get('BERRIES_CACHE_TTL'), 86400)
        self.__BERRIES_LOCK_TIMEOUT = parse_int(config.get('BERRIES_LOCK_TIMEOUT'), 300)
        self.__REDIS_URL = config.get('REDIS_URL', 'redis://localhost:6379/0')

app_settings = Settings(dotenv_values('.env'))

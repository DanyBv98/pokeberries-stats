import os

from dotenv import load_dotenv

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

    def __init__(self, env_path: str = '.env') -> None:
        load_dotenv(env_path)
        self.__EXTERNAL_API_ROOT = os.getenv('API_ROOT', 'https://pokeapi.co/api/v2')
        self.__BERRIES_CACHE_TTL = parse_int(os.getenv('BERRIES_CACHE_TTL', '86400'))
        self.__BERRIES_LOCK_TIMEOUT = parse_int(os.getenv('BERRIES_LOCK_TIMEOUT', '300'))
        self.__REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')

app_settings = Settings()

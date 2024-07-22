from enum import StrEnum


class RedisKeys(StrEnum):
    BERRIES = 'berries'
    BERRIES_LOCK = 'berries_requests'

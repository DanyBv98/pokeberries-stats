from dotenv import dotenv_values


class Settings:
    @property
    def EXTERNAL_API_ROOT(self):
        return self.__EXTERNAL_API_ROOT

    def __init__(self, config: dict[str, str | None]) -> None:
        self.__EXTERNAL_API_ROOT = config.get('API_ROOT', 'https://pokeapi.co/api/v2/')

app_settings = Settings(dotenv_values('.env'))

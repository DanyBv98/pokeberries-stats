from settings import app_settings


class ExternalUrls:
    @staticmethod
    def berries() -> str:
        return f'{app_settings.EXTERNAL_API_ROOT}/berry'

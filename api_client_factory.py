from settings import Settings
from api_client import ApiClient


class ApiClientFactory:

    def __init__(self, settings: Settings):
        self.__settings = settings
        self.__api_client = ApiClient(settings.profile_file_path)

    def get_api_client(self):
        return self.__api_client

from settings import Settings
from api_client import ApiClient


class ApiClientFactory:

    def __init__(self, settings: Settings):
        print('start init api client factory')
        self.__settings = settings
        self.__api_client = ApiClient(settings.profile_file_path)
        print('end init api client factory')

    def get_api_client(self):
        return self.__api_client

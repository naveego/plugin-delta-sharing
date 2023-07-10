import json
import os
from json import JSONEncoder
import pathlib


class Settings:

    def __init__(self, profile_file_path: str = "", share_credentials_version: int = -1, endpoint: str = "",
                 bearer_token: str = ""):
        self.profile_file_path = profile_file_path.strip()
        self.share_credentials_version = share_credentials_version
        self.endpoint = endpoint.strip()
        self.bearer_token = bearer_token.strip()

    def validate(self):
        print(self.to_string())
        incomplete_profile = True if self.share_credentials_version < 0 or len(self.endpoint) == 0 or len(
            self.bearer_token) == 0 else False
        if len(self.profile_file_path) == 0 and incomplete_profile:
            raise Exception('Incomplete profile')

        if len(self.profile_file_path) > 0:
            file_path_is_valid = os.path.isfile(self.profile_file_path)
            if not file_path_is_valid:
                raise Exception('Profile file path is not valid')
        else:
            # create file from the profile info
            self.__create_directory("config")

            # get last part of the endpoint
            account = self.endpoint.rsplit('/', 1)[-1]
            file_path = f'config/{account}.share'
            print(f'file name:{file_path}')
            profile_dict = {'shareCredentialsVersion': self.share_credentials_version, 'bearerToken': self.bearer_token,
                            'endpoint': self.endpoint}
            data_to_write = json.dumps(profile_dict)
            print(f'data to write:{data_to_write}')
            with open(file_path, 'w') as f:
                f.write(data_to_write)
            self.profile_file_path = file_path

    def get_profile_file_path(self):
        return self.profile_file_path

    def to_string(self):
        return f'{self.profile_file_path} | {self.share_credentials_version} | {self.endpoint} | {self.bearer_token}'

    @staticmethod
    def __create_directory(dir_path):
        pathlib.Path(dir_path).mkdir(parents=True, exist_ok=True)


class SettingsEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

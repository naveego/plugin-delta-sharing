import json
import pathlib

import publisher_pb2 as pb2
import publisher_pb2_grpc
from logger import PluginLogger

from server_status import ServerStatus
from api_client_factory import ApiClientFactory
from discover import get_all_schemas
from discover import get_refresh_schemas
from read import read_records
from settings import Settings


class Plugin(publisher_pb2_grpc.PublisherServicer):

    def __init__(self):
        self.__client_factory: ApiClientFactory = None
        self.__server: ServerStatus = ServerStatus()
        self.__logger: PluginLogger = None

    def Configure(self, request, context):
        # log_level = 1;
        # log_directory = 2;
        # permanent_directory = 3;
        # temporary_directory = 4;
        # data_versions = 5;

        # ensure all directories are created
        create_directory(request.temporary_directory)
        create_directory(request.permanent_directory)
        create_directory(request.log_directory)

        self.__logger = PluginLogger(request.log_directory)
        self.__logger.set_log_level(request.log_level)

        self.__server.config = request

        self.__logger.info(f'temp:{request.temporary_directory}, perm:{request.permanent_directory}, log dir:{request.log_directory}')

        return pb2.ConfigureResponse()

    def Connect(self, request, context):
        # settings_json = 2;
        # oauth_configuration = 3;
        # oauth_state_json = 4;
        # data_versions = 5;

        # settings_error = 1;
        # connection_error = 2;
        # oauth_error = 3;
        # oauth_state_json = 4;

        # self.__logger.set_log_prefix('connect')
        try:
            # print(f'load settings json, type:{type(request.settings_json)}')
            settings_dict = json.loads(request.settings_json)
            # print(f'settings json:{settings_dict}, type:{type(settings_dict)}, len:{len(settings_dict)}, '
            #       f'profile:{settings_dict["profile_file_path"]}')
            self.__server.settings = Settings(**settings_dict)
            # print(f'profile:{self.__server.settings.profile_file_path}')
            self.__server.settings.validate()
        except Exception as e:
            # print(f'error in processing load settings', e)
            return pb2.ConnectResponse(settings_error=str(e), connection_error='', oauth_error='',
                                       oauth_state_json=request.oauth_state_json)

        try:
            # print('get client from factory')
            self.__client_factory = ApiClientFactory(self.__server.settings)
            # print('received api client factory')
        except Exception as e:
            return pb2.ConnectResponse(settings_error='', connection_error=str(e), oauth_error='',
                                       oauth_state_json=request.oauth_state_json)

        # print('get client from factory')
        client = self.__client_factory.get_api_client()

        reachable = client.is_reachable
        # print(f'client is reachable:{reachable}')
        if not reachable:
            return pb2.ConnectResponse(settings_error='', connection_error='Not authorized', oauth_error='',
                                       oauth_state_json=request.oauth_state_json)

        self.__server.connected = True
        # print('server connected....')

        return pb2.ConnectResponse(settings_error='', connection_error='', oauth_error='',
                                   oauth_state_json=request.oauth_state_json)

    def DiscoverSchemas(self, request, context):

        # enum Mode
        # {
        #     ALL = 0;
        #     REFRESH = 1;
        # }
        # mode = 1;
        # to_refresh = 2;
        # sample_size = 4;

        # repeated Schema schemas = 1;
        # print('I am in the discover schema method')
        self.__logger.set_log_prefix('discover')
        self.__logger.info('Discovering Schemas...')
        discover_schemas_response = pb2.DiscoverSchemasResponse()

        sample_size = int(request.sample_size)
        # print(f'sample size:{sample_size}, request mode:{request.mode == pb2.DiscoverSchemasRequest.Mode.ALL}')
        if request.mode == pb2.DiscoverSchemasRequest.Mode.ALL:
            # print(f'mode all')
            try:
                schemas = get_all_schemas(self.__client_factory, sample_size)
                # print(f'total schemas returned:{len(schemas)}')
                discover_schemas_response.schemas.extend(schemas)
                # self.__logger.info(f'Schemas returned: {len(schemas)}')
            except Exception as e:
                self.__logger.error(str(e))
            return discover_schemas_response

        try:
            refresh_schemas = request.to_refresh
            self.__logger.info(f'Refresh schemas attempted: {len(refresh_schemas)}')

            schemas = get_refresh_schemas(self.__client_factory, refresh_schemas, sample_size)
            discover_schemas_response.schemas.extend(list(schemas))

            self.__logger.info(f'schemas returned: {len(discover_schemas_response)}')
        except Exception as e:
            self.__logger.error(str(e))
        return discover_schemas_response

    def ReadStream(self, request, context):
        try:
            schema = request.schema
            limit = request.limit
            limit_flag = limit != 0
            job_id = request.job_id
            records_count = 0

            self.__logger.set_log_prefix(job_id)

            records = read_records(self.__client_factory, schema, limit)

            for record in records:
                if (limit_flag and records_count == limit) or not self.__server.connected:
                    break
                records_count += 1
                yield record

        except Exception as e:
            self.__logger.error(str(e))


def create_directory(dir_path):
    pathlib.Path(dir_path).mkdir(parents=True, exist_ok=True)

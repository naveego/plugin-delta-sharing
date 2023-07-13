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
        try:
            # ensure all directories are created
            create_directory(request.temporary_directory)
            create_directory(request.permanent_directory)
            create_directory(request.log_directory)

            self.__logger = PluginLogger(log_path=request.log_directory)
            self.__logger.set_log_level(request.log_level)

            self.__server.config = request

        except Exception as e:
            print(f'error in configure:{e}')
        return pb2.ConfigureResponse()

    def Connect(self, request, context):
        self.__logger.set_log_prefix('connect')
        try:
            settings_dict = json.loads(request.settings_json)
            self.__server.settings = Settings(**settings_dict)
            self.__server.settings.validate()
        except Exception as e:
            return pb2.ConnectResponse(settings_error=str(e), connection_error='', oauth_error='',
                                       oauth_state_json=request.oauth_state_json)

        try:
            self.__client_factory = ApiClientFactory(self.__server.settings)
        except Exception as e:
            return pb2.ConnectResponse(settings_error='', connection_error=str(e), oauth_error='',
                                       oauth_state_json=request.oauth_state_json)

        client = self.__client_factory.get_api_client()

        reachable = client.is_reachable
        if not reachable:
            return pb2.ConnectResponse(settings_error='', connection_error='Not authorized', oauth_error='',
                                       oauth_state_json=request.oauth_state_json)

        self.__server.connected = True
        return pb2.ConnectResponse(settings_error='', connection_error='', oauth_error='',
                                   oauth_state_json=request.oauth_state_json)

    def ConnectSession(self, request, context):
        self.__logger.set_log_prefix('connect_session')
        self.__logger.info('Connecting session...')

        yield self.Connect(request, context)
        self.__logger.info('Session Connected.')

    def DiscoverSchemas(self, request, context):
        self.__logger.set_log_prefix('discover')
        self.__logger.info('Discovering Schemas...')
        discover_schemas_response = pb2.DiscoverSchemasResponse()

        sample_size = int(request.sample_size)
        if request.mode == pb2.DiscoverSchemasRequest.Mode.ALL:
            try:
                schemas = get_all_schemas(self.__client_factory, sample_size)
                discover_schemas_response.schemas.extend(schemas)
            except Exception as e:
                self.__logger.error(str(e), context)
            return discover_schemas_response

        try:
            refresh_schemas = request.to_refresh
            self.__logger.info(f'Refresh schemas attempted: {len(refresh_schemas)}')

            schemas = get_refresh_schemas(self.__client_factory, refresh_schemas, sample_size)
            discover_schemas_response.schemas.extend(list(schemas))

            self.__logger.info(f'schemas returned: {len(discover_schemas_response.schemas)}')
        except Exception as e:
            self.__logger.error(str(e), context)
        return discover_schemas_response

    def DiscoverShapes(self, request, context):
        return pb2.DiscoverSchemasResponse()

    def Disconnect(self, request, context):
        self.__server.connected = False
        self.__server.settings = None
        self.__logger.info('Disconnected')
        return pb2.DisconnectResponse()

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
            self.__logger.error(str(e), context)


def create_directory(dir_path):
    pathlib.Path(dir_path).mkdir(parents=True, exist_ok=True)

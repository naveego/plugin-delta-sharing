import json
import grpc
import datetime

import publisher_pb2 as pb2
import publisher_pb2_grpc as pb2_grpc
from settings import Settings, SettingsEncoder
import unittest
import os
import sys


def get_wrong_settings():
    return Settings(profile_file_path='wrong_config.share')


def get_settings():
    return Settings(profile_file_path='config.share')


def get_settings_from_profile_info():
    return Settings(share_credentials_version=1,
                    endpoint="https://westus.azuredatabricks.net/api/2.0/delta-sharing/metastores/2c5f2daa-0e34-4c1f-a9f4-ec3d1a98912f",
                    bearer_token="mfoQi9FZqLwztP-hIclbEo7MFP2TbG6ACqYa9R66mX5Pxwu47Fdk-oYCuTTjpNx2")


class DeltaSharingIntegrationTestClient(unittest.TestCase):
    grpc_port = 49000

    def test_connect_with_profile_file(self):
        channel = grpc.insecure_channel("localhost:" + str(self.grpc_port))
        stub = pb2_grpc.PublisherStub(channel)

        configure_request = pb2.ConfigureRequest()
        config_response = stub.Configure(configure_request)
        self.assertIsInstance(config_response, pb2.ConfigureResponse)

        settings = get_settings()
        settings_json = json.dumps(settings, cls=SettingsEncoder)
        connect_request = pb2.ConnectRequest(settings_json=settings_json, oauth_state_json='')
        connect_response = stub.Connect(connect_request)
        self.assertIsInstance(connect_response, pb2.ConnectResponse)
        self.assertEqual(connect_response.settings_error, '')
        self.assertEqual(connect_response.connection_error, '')
        self.assertEqual(connect_response.oauth_error, '')

    def test_connect_with_profile_info(self):
        channel = grpc.insecure_channel("localhost:" + str(self.grpc_port))
        stub = pb2_grpc.PublisherStub(channel)

        configure_request = pb2.ConfigureRequest()
        stub.Configure(configure_request)

        settings = get_settings_from_profile_info()
        settings_json = json.dumps(settings, cls=SettingsEncoder)
        connect_request = pb2.ConnectRequest(settings_json=settings_json, oauth_state_json='')
        connect_response = stub.Connect(connect_request)
        self.assertIsInstance(connect_response, pb2.ConnectResponse)
        self.assertEqual(connect_response.settings_error, '')
        self.assertEqual(connect_response.connection_error, '')
        self.assertEqual(connect_response.oauth_error, '')

    def test_failed_connect(self):
        channel = grpc.insecure_channel("localhost:" + str(self.grpc_port))
        stub = pb2_grpc.PublisherStub(channel)

        configure_request = pb2.ConfigureRequest()
        stub.Configure(configure_request)

        settings = get_wrong_settings()
        settings_json = json.dumps(settings, cls=SettingsEncoder)
        connect_request = pb2.ConnectRequest(settings_json=settings_json, oauth_state_json='')
        connect_response = stub.Connect(connect_request)
        self.assertIsInstance(connect_response, pb2.ConnectResponse)
        print(f'settings:{connect_response.settings_error}, connect:{connect_response.connection_error}, '
              f'oauth:{connect_response.oauth_error}')
        self.assertTrue(len(connect_response.settings_error) > 0 or len(connect_response.connection_error) > 0
                        or len(connect_response.oauth_error) > 0)

    def test_discover_all_schemas(self):
        channel = grpc.insecure_channel("localhost:" + str(self.grpc_port))
        stub = pb2_grpc.PublisherStub(channel)

        configure_request = pb2.ConfigureRequest()
        stub.Configure(configure_request)

        settings = get_settings()
        settings_json = json.dumps(settings, cls=SettingsEncoder)
        print(f'settings json:{settings_json}')
        connect_request = pb2.ConnectRequest(settings_json=settings_json, oauth_state_json='')
        print('connect request created..')
        stub.Connect(connect_request)

        print('connect response..')

        request = pb2.DiscoverSchemasRequest(mode=pb2.DiscoverSchemasRequest.Mode.ALL, sample_size=10)
        response = stub.DiscoverSchemas(request)

        print(f'{datetime.datetime.now()} final response: {len(response.schemas)}')
        self.assertIsInstance(response, pb2.DiscoverSchemasResponse)
        self.assertEqual(47, len(response.schemas))

        schema = response.schemas[0]
        print(f'schema is:{schema.id}, name:{schema.name}, query:{schema.query}, sample:{len(schema.sample)}, '
              f'properties:{len(schema.properties)}')
        print(f'schema test done....')
        self.assertEqual(schema.id, 'share_safe_1_credi.dataaccess_schema.da_consumer_loan_officers')
        self.assertEqual(schema.name, 'share_safe_1_credi.dataaccess_schema.da_consumer_loan_officers')
        self.assertEqual(len(schema.sample), 10)
        self.assertEqual(len(schema.properties), 23)

        column = schema.properties[0]
        print(f'column:{column.id}, name:{column.name}, type:{column.type}')
        self.assertEqual(column.id, 'organization_internal_id')
        self.assertEqual(column.name, 'organization_internal_id')
        self.assertEqual(column.type, pb2.PropertyType.STRING)

        column = schema.properties[22]
        print(f'column:{column.id}, name:{column.name}, type:{column.type}')
        self.assertEqual(column.id, 'Extraction_Run_Date')
        self.assertEqual(column.name, 'Extraction_Run_Date')
        self.assertEqual(column.type, pb2.PropertyType.DATETIME)

    def test_discover_refresh_schema(self):
        channel = grpc.insecure_channel("localhost:" + str(self.grpc_port))
        stub = pb2_grpc.PublisherStub(channel)

        configure_request = pb2.ConfigureRequest()
        stub.Configure(configure_request)

        settings = get_settings()
        settings_json = json.dumps(settings, cls=SettingsEncoder)
        print(f'settings json:{settings_json}')
        connect_request = pb2.ConnectRequest(settings_json=settings_json, oauth_state_json='')
        print('connect request created..')
        stub.Connect(connect_request)

        print('connect response..')
        refresh_schema = pb2.Schema(id='share_safe_1_credi.dataaccess_schema.da_consumer_loan_officers')

        request = pb2.DiscoverSchemasRequest(mode=pb2.DiscoverSchemasRequest.Mode.REFRESH, to_refresh=[refresh_schema],
                                             sample_size=5)
        response = stub.DiscoverSchemas(request)

        print(f'{datetime.datetime.now()} final response: {len(response.schemas)}')
        self.assertIsInstance(response, pb2.DiscoverSchemasResponse)
        self.assertEqual(1, len(response.schemas))

        schema = response.schemas[0]
        print(f'schema is:{schema.id}, name:{schema.name}, query:{schema.query}, sample:{len(schema.sample)}, '
              f'properties:{len(schema.properties)}')
        print(f'schema test done....')
        self.assertEqual(schema.id, 'share_safe_1_credi.dataaccess_schema.da_consumer_loan_officers')
        # self.assertEqual(schema.name, 'share_safe_1_credi.dataaccess_schema.da_consumer_loan_officers')
        self.assertEqual(len(schema.sample), 5)
        self.assertEqual(len(schema.properties), 23)

        column = schema.properties[0]
        print(f'column:{column.id}, name:{column.name}, type:{column.type}')
        self.assertEqual(column.id, 'organization_internal_id')
        self.assertEqual(column.name, 'organization_internal_id')
        self.assertEqual(column.type, pb2.PropertyType.STRING)

        column = schema.properties[22]
        print(f'column:{column.id}, name:{column.name}, type:{column.type}')
        self.assertEqual(column.id, 'Extraction_Run_Date')
        self.assertEqual(column.name, 'Extraction_Run_Date')
        self.assertEqual(column.type, pb2.PropertyType.DATETIME)

    def test_discover_refresh_schemas(self):
        channel = grpc.insecure_channel("localhost:" + str(self.grpc_port))
        stub = pb2_grpc.PublisherStub(channel)

        configure_request = pb2.ConfigureRequest()
        stub.Configure(configure_request)

        settings = get_settings()
        settings_json = json.dumps(settings, cls=SettingsEncoder)
        print(f'settings json:{settings_json}')
        connect_request = pb2.ConnectRequest(settings_json=settings_json, oauth_state_json='')
        print('connect request created..')
        stub.Connect(connect_request)

        print('connect response..')
        refresh_schemas = [pb2.Schema(id='share_safe_1_credi.dataaccess_schema.da_consumer_loan_officers'),
                           pb2.Schema(id='share_safe_1_credi.dataaccess_schema.da_monthly_debt')]

        request = pb2.DiscoverSchemasRequest(mode=pb2.DiscoverSchemasRequest.Mode.REFRESH, to_refresh=refresh_schemas,
                                             sample_size=5)
        response = stub.DiscoverSchemas(request)

        print(f'{datetime.datetime.now()} final response: {len(response.schemas)}')
        self.assertIsInstance(response, pb2.DiscoverSchemasResponse)
        self.assertEqual(2, len(response.schemas))

        schema = response.schemas[0]
        print(f'schema is:{schema.id}, name:{schema.name}, query:{schema.query}, sample:{len(schema.sample)}, '
              f'properties:{len(schema.properties)}')
        print(f'schema test done....')
        self.assertEqual(schema.id, 'share_safe_1_credi.dataaccess_schema.da_consumer_loan_officers')
        # self.assertEqual(schema.name, 'share_safe_1_credi.dataaccess_schema.da_consumer_loan_officers')
        self.assertEqual(len(schema.sample), 5)
        self.assertEqual(len(schema.properties), 23)

        column = schema.properties[0]
        print(f'column:{column.id}, name:{column.name}, type:{column.type}')
        self.assertEqual(column.id, 'organization_internal_id')
        self.assertEqual(column.name, 'organization_internal_id')
        self.assertEqual(column.type, pb2.PropertyType.STRING)

        column = schema.properties[22]
        print(f'column:{column.id}, name:{column.name}, type:{column.type}')
        self.assertEqual(column.id, 'Extraction_Run_Date')
        self.assertEqual(column.name, 'Extraction_Run_Date')
        self.assertEqual(column.type, pb2.PropertyType.DATETIME)

    def test_read_stream_full_table(self):
        channel = grpc.insecure_channel("localhost:" + str(self.grpc_port))
        stub = pb2_grpc.PublisherStub(channel)

        settings = get_settings_from_profile_info()
        settings_json = json.dumps(settings, cls=SettingsEncoder)
        connect_request = pb2.ConnectRequest(settings_json=settings_json, oauth_state_json='')
        stub.Connect(connect_request)

        schema = pb2.Schema(id='share_safe_1_credi.dataaccess_schema.da_monthly_debt')
        read_request = pb2.ReadRequest(schema=schema)
        records = stub.ReadStream(read_request)

        data_count = 0
        for record in records:
            data_count += 1

        # the total count of the test table may change over time, so change the hardcoded 144547 to the actual one
        self.assertEqual(144547, data_count)

    def test_read_stream_limit(self):
        channel = grpc.insecure_channel("localhost:" + str(self.grpc_port))
        stub = pb2_grpc.PublisherStub(channel)

        settings = get_settings_from_profile_info()
        settings_json = json.dumps(settings, cls=SettingsEncoder)
        connect_request = pb2.ConnectRequest(settings_json=settings_json, oauth_state_json='')
        stub.Connect(connect_request)

        schema = pb2.Schema(id='share_safe_1_credi.dataaccess_schema.da_monthly_debt')
        read_request = pb2.ReadRequest(schema=schema, limit=23)
        records = stub.ReadStream(read_request)

        data = []
        for record in records:
            data.append(record)

        self.assertEqual(23, len(data))


if __name__ == '__main__':
    DeltaSharingIntegrationTestClient.grpc_port = 36657  # edit the port where server starts
    print(
        f'{datetime.datetime.now()} Server started....now listen to channel at port:{DeltaSharingIntegrationTestClient.grpc_port}')
    # DeltaSharingIntegrationTestClient.discover_all_schemas_test(grpc_port)
    unittest.main()

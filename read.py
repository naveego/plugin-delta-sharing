import delta_sharing
import json
import publisher_pb2 as pb2
from api_client_factory import ApiClientFactory


class Read:
    pass


# def read_dataframes(api_client_factory: ApiClientFactory, schema: pb2.Schema, limit: int = 0):
#     print(f'in read dataframes..')
#     print(f'is schema null:{schema.id}')
#     table_url = api_client_factory.get_api_client().profile_file + f'#{schema.id}'
#     print(f'table url in read records:{table_url}')
#     if limit <= 0:
#         df = delta_sharing.load_as_pandas(table_url)
#     else:
#         df = delta_sharing.load_as_pandas(table_url, limit=limit)
#     print(f'come back from delta api: {len(df)}')
#     return df


def read_records(api_client_factory: ApiClientFactory, schema: pb2.Schema, limit: int = 0):
    print(f'in read records..limit:{limit}')
    print(f'is schema null:{schema.id}')
    table_url = api_client_factory.get_api_client().profile_file + f'#{schema.id}'
    print(f'table url in read records:{table_url}')
    if limit <= 0:
        df = delta_sharing.load_as_pandas(table_url)
    else:
        df = delta_sharing.load_as_pandas(table_url, limit=limit)
    print(f'come back from delta api: {len(df)}')

    for index, record in df.iterrows():
        data = json.dumps(record.to_dict(), default=str)
        record = pb2.Record(data_json=data)
        yield record

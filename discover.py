from api_client_factory import ApiClientFactory
import delta_sharing
import publisher_pb2 as pb2
from concurrent.futures import wait
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import json
import numpy


def get_type(data_type: str) -> pb2.PropertyType:
    try:
        data_type = data_type.lower()
        if 'object' in data_type or 'string' in data_type:
            return pb2.PropertyType.STRING
        elif 'float' in data_type:
            return pb2.PropertyType.FLOAT
        elif 'int' in data_type:
            return pb2.PropertyType.INTEGER
        elif 'datetime' in data_type:
            return pb2.PropertyType.DATETIME
        elif 'bool' in data_type:
            return pb2.PropertyType.BOOL
        else:
            return pb2.PropertyType.STRING
    except Exception as e:
        print(f'in get type:{e}')


def read_df(table_url, limit):
    if limit < 0:
        df = delta_sharing.load_as_pandas(table_url)
    else:
        df = delta_sharing.load_as_pandas(table_url, limit=limit)

    df = df.replace(numpy.nan, None)

    return df


def get_all_schemas_concurrent(api_client_factory: ApiClientFactory, sample_size: int = 5):
    api_client = api_client_factory.get_api_client()
    schemas = []
    tables = api_client.sharing_client.list_all_tables()

    # executor = ProcessPoolExecutor(10)
    schema = None

    with ProcessPoolExecutor(max_workers=10) as executor:
        futures = []
        for table in tables:
            schema_id = f'{table.share}.{table.schema}.{table.name}'
            schema = pb2.Schema(id=schema_id, name=schema_id, data_flow_direction=pb2.Schema.DataFlowDirection.READ)

            table_url = api_client.profile_file + f'#{schema_id}'

            future = executor.submit(read_df, table_url, sample_size)
            futures.append(future)
            schemas.append(schema)

        wait(futures)

        for idx, future in enumerate(futures):
            df = future.result()
            schema = schemas[idx]
            try:
                for col in df.columns:
                    type_at_source = str(df[col].dtype)
                    type_at_dest = get_type(type_at_source)
                    column_property = pb2.Property(id=str(col), name=str(col), type=type_at_dest, type_at_source=type_at_source)
                    schema.properties.append(column_property)

                for index, record in df.iterrows():
                    data = json.dumps(record.to_dict(), default=str)
                    record = pb2.Record(data_json=data)
                    schema.sample.append(record)
            except Exception as e:
                print(f'error in discover:{e}')
    executor.shutdown(wait=False)

    return schemas


def get_all_schemas(api_client_factory: ApiClientFactory, sample_size: int = 5):
    api_client = api_client_factory.get_api_client()
    schemas = []
    tables = api_client.sharing_client.list_all_tables()

    schema = None

    for table in tables:
        schema_id = f'{table.share}.{table.schema}.{table.name}'
        schema = pb2.Schema(id=schema_id, name=schema_id, data_flow_direction=pb2.Schema.DataFlowDirection.READ)
        schemas.append(schema)

        table_url = api_client.profile_file + f'#{schema_id}'

        df = read_df(table_url, sample_size)
        try:
            for col in df.columns:
                type_at_source = str(df[col].dtype)
                type_at_dest = get_type(type_at_source)
                column_property = pb2.Property(id=str(col), name=str(col), type=type_at_dest, type_at_source=type_at_source)
                schema.properties.append(column_property)

            for index, record in df.iterrows():
                data = json.dumps(record.to_dict(), default=str)
                record = pb2.Record(data_json=data)
                schema.sample.append(record)
        except Exception as e:
            print(f'error in discover:{e}')
    return schemas


def get_count_of_records(api_client_factory: ApiClientFactory, schema: pb2.Schema):
    return pb2.Count.Kind.UNAVAILABLE


def get_refresh_schema_for_table(api_client_factory: ApiClientFactory, schema, sample_size: int = 5):
    api_client = api_client_factory.get_api_client()
    table_url = api_client.profile_file + f'#{schema.id}'
    df = read_df(table_url, sample_size)
    del schema.properties[:]

    try:
        for col in df.columns:
            type_at_source = str(df[col].dtype)
            type_at_dest = get_type(type_at_source)
            column_property = pb2.Property(id=str(col), name=str(col), type=type_at_dest, type_at_source=type_at_source)
            schema.properties.append(column_property)

        for index, record in df.iterrows():
            data = json.dumps(record.to_dict(), default=str)
            record = pb2.Record(data_json=data)
            schema.sample.append(record)

    except Exception as e:
        print(f'error in discover:{e}')

    return schema


def get_refresh_schemas(api_client_factory: ApiClientFactory, refresh_schemas, sample_size: int = 5):
    for schema in refresh_schemas:
        yield get_refresh_schema_for_table(api_client_factory, schema, sample_size)



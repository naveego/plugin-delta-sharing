import sys

import grpc

import publisher_pb2_grpc as pb2_grpc
from logger import PluginLogger

from concurrent import futures
from plugin_service import Plugin

if __name__ == '__main__':

    logger = PluginLogger()

    try:

        # create new server and start it
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        pb2_grpc.add_PublisherServicer_to_server(Plugin(), server)
        port = server.add_insecure_port("[::]:0")
        server.start()

        # write out the connection information for the Hashicorp plugin runner
        output = f'1|1|tcp|localhost:{port}|grpc'
        print(output)
        sys.stdout.flush()
        logger.info(f'Started on port {port}')

        # wait to exit while given input
        input()

        logger.info('Plugin exiting.....')

        # shutdown server
        server.wait_for_termination(1)

    except Exception as e:
        logger.error(str(e))
        raise Exception('Error in running plugin server')

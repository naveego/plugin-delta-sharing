import grpc
from concurrent import futures
import publisher_pb2_grpc as pb2_grpc
from plugin_service import Plugin


class DeltaSharingIntegrationTestServer:

    def __init__(self):
        pass

    @staticmethod
    def start_server():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
        pb2_grpc.add_PublisherServicer_to_server(Plugin(), server)
        port = server.add_insecure_port("[::]:0")
        # port = server.add_insecure_port("[::]:49000")
        server.start()
        print("starting server at port:", port)
        server.wait_for_termination()


if __name__ == '__main__':
    print('Testing grpc server delta_sharing_test')
    DeltaSharingIntegrationTestServer.start_server()

import publisher_pb2 as pb2
from settings import Settings


class ServerStatus:

    def __init__(self, config: pb2.ConfigureRequest = None, settings: Settings = None, connected: bool = False):
        self.config = config
        self.settings = settings
        self.connected = connected

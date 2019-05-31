from comm.socket_wrapper import SocketWrapper
from common.shippo_symbols import PROTOCOL_HELO_COMMAND, PROTOCOL_QUIT_COMMAND
from common.utilities import Utilities

class SessionManager(object):
    def Open(self):
        if not self.__session:
            return False
        self.__session.Send(PROTOCOL_HELO_COMMAND)
        Utilities.PrintTheStuffTheClientSent(PROTOCOL_HELO_COMMAND)
        response = self.__session.Receive()
        Utilities.PrintTheStuffTheServerRepliedWith(response)
        return response.startswith("200 OK.")
            
    def Close(self):
        if not self.__session:
            return False
        self.__session.Send(PROTOCOL_QUIT_COMMAND)
        Utilities.PrintTheStuffTheClientSent(PROTOCOL_QUIT_COMMAND)
        response = self.__session.Receive()
        Utilities.PrintTheStuffTheServerRepliedWith(response)
        result = response.startswith("206 OK.")
        self.__session.Close()
        return result
    
    def __init__(self, hostname, port):
        self.__hostname = hostname
        self.__port = port
        self.__session = SocketWrapper(hostname, port)
        pass
    
    def __enter__(self):
        self.__session.__enter__()
        return self
    
    def __exit__(self, exc_type, exc_value, tb):
        self.__exc_type = exc_type
        self.__exc_value = exc_value
        self.__tb = tb
        return self.Close()
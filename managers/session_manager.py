from comm.socket_wrapper import SocketWrapper
from common.shippo_symbols import PROTOCOL_HELO_COMMAND, PROTOCOL_QUIT_COMMAND, \
    PROTOCOL_LIST_COMMAND
from common.utilities import Utilities


class SessionManager(object):
    
    def GetResponseLines(self):
        return self.__responseLines

    def Open(self):
        if not self.__session:
            return False
        self.__session.Send(PROTOCOL_HELO_COMMAND)
        Utilities.PrintTheStuffTheClientSent(PROTOCOL_HELO_COMMAND)
        response = self.__session.Receive()
        Utilities.PrintTheStuffTheServerRepliedWith(response)
        return response.startswith("200 OK.")
            
    def ListRemoteProcesses(self):
        if not self.__session:
            return False
        self.__session.Send(PROTOCOL_LIST_COMMAND)
        Utilities.PrintTheStuffTheClientSent(PROTOCOL_LIST_COMMAND)
        response = self.__session.Receive()
        Utilities.PrintTheStuffTheServerRepliedWith(response)
        self.__responseLines = self.__session.ReceiveAllLines()
        for strCurLine in self.__responseLines:
            Utilities.PrintTheStuffTheServerRepliedWith(strCurLine)
        return response.startswith("204")
            
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

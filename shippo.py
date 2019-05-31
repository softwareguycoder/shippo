#!/usr/bin/python3

from common.utilities import Utilities
from comm.socket_wrapper import SocketWrapper
from common.shippo_symbols import TCP_IP, TCP_PORT, \
    PROTOCOL_HELO_COMMAND, PROTOCOL_QUIT_COMMAND, EXIT_SUCCESS


def main():
    with SocketWrapper(TCP_IP, TCP_PORT) as clientConn:
        clientConn.Send(PROTOCOL_HELO_COMMAND)
        Utilities.PrintTheStuffTheClientSent(PROTOCOL_HELO_COMMAND)        
        Utilities.PrintTheStuffTheServerRepliedWith(clientConn.Receive())
    
        clientConn.Send(PROTOCOL_QUIT_COMMAND)
        Utilities.PrintTheStuffTheClientSent(PROTOCOL_QUIT_COMMAND)        
        Utilities.PrintTheStuffTheServerRepliedWith(clientConn.Receive())
    
    exit(EXIT_SUCCESS)

    
if __name__ == "__main__":
    main()

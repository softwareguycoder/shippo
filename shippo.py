#!/usr/bin/python3

from common.utilities import Utilities
from comm.socket_wrapper import SocketWrapper
from common.shippo_symbols import TCP_IP, TCP_PORT, \
    PROTOCOL_HELO_COMMAND, PROTOCOL_QUIT_COMMAND, EXIT_SUCCESS


def main():
    clientSocket = SocketWrapper()
    clientSocket.Connect(TCP_IP, TCP_PORT)
    
    clientSocket.Send(PROTOCOL_HELO_COMMAND)
    Utilities.PrintTheStuffTheClientSent(PROTOCOL_HELO_COMMAND)        
    Utilities.PrintTheStuffTheServerRepliedWith(clientSocket.Receive())
    
    clientSocket.Send(PROTOCOL_QUIT_COMMAND)
    Utilities.PrintTheStuffTheClientSent(PROTOCOL_QUIT_COMMAND)        
    Utilities.PrintTheStuffTheServerRepliedWith(clientSocket.Receive())
    
    clientSocket.Close()        
    exit(EXIT_SUCCESS)

    
if __name__ == "__main__":
    main()

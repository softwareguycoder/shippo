#!/usr/bin/python3
from managers.session_manager import SessionManager
from common.shippo_symbols import TCP_IP, TCP_PORT, EXIT_SUCCESS, EXIT_FAILURE
from common.utilities import Utilities

def main():
    with SessionManager(TCP_IP, TCP_PORT) as session:
        if not session.Open():
            exit(EXIT_FAILURE)
        if not session.ListRemoteProcesses():
            exit(EXIT_FAILURE)
        responseLines = session.GetResponseLines()
        for line in responseLines:
            Utilities.PrintTheStuffTheServerRepliedWith(line)
                
    exit(EXIT_SUCCESS)

    
if __name__ == "__main__":
    main()

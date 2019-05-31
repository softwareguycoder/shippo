#!/usr/bin/python3
from managers.session_manager import SessionManager
from common.shippo_symbols import TCP_IP, TCP_PORT, EXIT_SUCCESS

def main():
    with SessionManager(TCP_IP, TCP_PORT) as session:
        session.Open()
        session.ListRemoteProcesses()
    
    exit(EXIT_SUCCESS)

    
if __name__ == "__main__":
    main()

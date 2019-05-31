#!/usr/bin/python3
from managers.conn_manager import ConnectionManager
from common.shippo_symbols import TCP_IP, TCP_PORT, EXIT_SUCCESS

def main():
    with ConnectionManager(TCP_IP, TCP_PORT) as session:
        session.Open()
    
    exit(EXIT_SUCCESS)

    
if __name__ == "__main__":
    main()

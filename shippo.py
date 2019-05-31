#!/usr/bin/python3

import socket

ASCII_ENCODING = 'ascii'
BUFFER_SIZE = 1024
BYTES_SENT_FORMAT = "B sent."
ERROR_FAILED_SEND_HELO_COMMAND = \
    "ERROR: Failed to send HELO command to the server."
ERROR_FAILED_SEND_QUIT_COMMAND = \
    "ERROR: Failed to send QUIT command to the server."
EXIT_FAILURE = -1
EXIT_SUCCESS = 0
PROTOCOL_HELO_COMMAND = "HELO\n".encode(ASCII_ENCODING)
PROTOCOL_QUIT_COMMAND = "QUIT\n".encode(ASCII_ENCODING)
TCP_IP = '127.0.0.1'
TCP_PORT = 9000
SERVER_DATA_FORMAT = "S: {}"

def DoConnect(clientSocket):
    result = False
    if clientSocket is None:
        return result
    try:
        clientSocket.connect((TCP_IP, TCP_PORT))
    except Exception as e:
        print("ERROR: Failed to connect to server.\n", e)
        result = False
    else:
        result = True
        
    return result


def DoSend(clientSocket, bytesToSend):
    result = 0  # bytes sent
    if (len(bytesToSend) == 0):
        return result
    try:
        result = clientSocket.send(bytesToSend)
    except:
        result = 0

    return result


def main():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if not DoConnect(clientSocket):
        exit(EXIT_FAILURE)
    bytesSent = DoSend(clientSocket, PROTOCOL_HELO_COMMAND)
    if bytesSent == 0:
        print(ERROR_FAILED_SEND_HELO_COMMAND)
        clientSocket.close()
        exit(EXIT_FAILURE)
        
    print(bytesSent, BYTES_SENT_FORMAT)
    receivedData = clientSocket.recv(BUFFER_SIZE).decode(ASCII_ENCODING).strip()
    receivedDataLen = len(receivedData)
    
    print(SERVER_DATA_FORMAT.format(
        receivedDataLen, 
        receivedData))
    
    bytesSent = DoSend(clientSocket, PROTOCOL_QUIT_COMMAND)
    if bytesSent == 0:
        print(ERROR_FAILED_SEND_QUIT_COMMAND)
        clientSocket.close()
        exit(EXIT_FAILURE)
    
    print(bytesSent, BYTES_SENT_FORMAT)
    receivedData = clientSocket.recv(BUFFER_SIZE).decode(ASCII_ENCODING).strip()
    receivedDataLen = len(receivedData)
    
    print(SERVER_DATA_FORMAT.format( 
        receivedDataLen, 
        receivedData))
    
    clientSocket.close()        
    exit(EXIT_SUCCESS)

    
if __name__ == "__main__":
    main()

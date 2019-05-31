#!/usr/bin/python3

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 9000
BUFFER_SIZE = 1024
PROTOCOL_HELO_COMMAND = "HELO\n".encode('ascii')
EXIT_FAILURE = -1
EXIT_SUCCESS = 0


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
        print("ERROR: Failed to send HELO command to the server.")
        exit(EXIT_FAILURE)
        
    print(bytesSent, " B sent.")
    receivedData = clientSocket.recv(BUFFER_SIZE)
    clientSocket.close()

    print("received data:", receivedData)
    exit(EXIT_SUCCESS)

    
if __name__ == "__main__":
    main()

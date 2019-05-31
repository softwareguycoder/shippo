from common.shippo_symbols import ERROR_FAILED_CONNECT_TO_SERVER_FORMAT, \
    EXIT_FAILURE, ASCII_ENCODING, ERROR_FAILED_SEND_MESSAGE_FORMAT, \
    BUFFER_SIZE, ERROR_FAILED_RECEIVE_FROM_SERVER_FORMAT
import socket


class SocketWrapper(object):

    def __DoReceive(self):
        strReply = ''
        if self.__clientSocket is None:
            return strReply
        try:
            strReply = self.__clientSocket.recv(BUFFER_SIZE) \
                .decode(ASCII_ENCODING).strip()
        except Exception as e:
            print(ERROR_FAILED_RECEIVE_FROM_SERVER_FORMAT.format(e))
            strReply = ''
        
        return strReply
       
    def __DoSend(self, bytesToSend):
        result = 0  # bytes sent
        if (len(bytesToSend) == 0):
            return result
        if self.__clientSocket is None:
            return result
        try:
            self.__clientSocket.sendall(bytesToSend)
            result = len(bytesToSend)
        except:
            result = 0
    
        return result

    def __DoConnect(self, hostname, port):
        result = False
        if self.__clientSocket is None:
            return result
        try:
            self.__clientSocket.connect((hostname, port))
        except Exception as e:
            print(ERROR_FAILED_CONNECT_TO_SERVER_FORMAT.format(e))
            result = False
        else:
            result = True
            
        return result
    
    def Receive(self):
        strReply = self.__DoReceive()
        if len(strReply.strip()) == 0:
            self.Close()
            exit(EXIT_FAILURE)
            
        return strReply
    
    def Send(self, strMessage):
        bytesSent = 0
        if len(strMessage.strip()) == 0:
            return bytesSent
        bytesSent = self.__DoSend(strMessage.encode(ASCII_ENCODING))
        if bytesSent <= 0:
            self.Close()
            print(ERROR_FAILED_SEND_MESSAGE_FORMAT.
                  format(strMessage))
            exit(EXIT_FAILURE)
            
        return bytesSent
    
    def Close(self):
        if self.__clientSocket is None:
            return
        self.__clientSocket.close()
        self.__clientSocket = None
        pass

    def Connect(self, hostname, port):
        result = self.__DoConnect(hostname, port)
        if not result:
            self.Close()
            exit(EXIT_FAILURE)
        pass

    def __init__(self):
        self.__clientSocket = \
            socket.socket(socket.AF_INET, socket.SOCK_STREAM)

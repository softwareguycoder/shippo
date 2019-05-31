from common.shippo_symbols import SERVER_DATA_FORMAT, CLIENT_DATA_FORMAT


class Utilities(object):
    
    @staticmethod
    def PrintTheStuffTheClientSent(strMessage):
        if len(strMessage.strip()) == 0:
            return
        print(CLIENT_DATA_FORMAT.format(strMessage.strip(),
            len(strMessage)))
        pass
    
    @staticmethod
    def PrintTheStuffTheServerRepliedWith(receivedData):
        if len(receivedData) == 0:
            return
        
        print(SERVER_DATA_FORMAT.format(
            receivedData, len(receivedData)))
        pass
    
    

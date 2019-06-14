
class ListUtilities(object):
    @staticmethod
    def FormatEltsSeparatedBy(char, theList):
        if not len(char.strip()):
            return ''
        return str(char).join(map(str, theList))
    
    @staticmethod
    def PrintEltsSeparatedBy(char, theList):
        print(str(char).join(map(str,theList)))
        pass

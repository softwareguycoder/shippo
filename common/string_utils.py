class StringUtilities(object):

        @staticmethod
        def IsNullOrWhiteSpace(value):
            if not isinstance(value, str):
                return False
            # assume value is a string
            return value == '' or len(value.strip()) == 0
                
            

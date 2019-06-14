from common.string_utils import StringUtilities
from common.list_utils import ListUtilities

PROMPT_FORMAT = "> {} ({})[{}]: > "

class Prompter(object):    
    @staticmethod
    def __DoDisplayPrompt(strPrompt, pvDefault, choiceValueSet=[], 
                        inputValidator=None, invalidInputHandler=None):
        try:
            if StringUtilities.IsNullOrWhiteSpace(strPrompt):
                return pvDefault
            strPromptFormat = PROMPT_FORMAT
            if StringUtilities.IsNullOrWhiteSpace(pvDefault):
                strPromptFormat = strPromptFormat.replace("[{}]", '')
            if not len(choiceValueSet):
                strPromptFormat = strPromptFormat.replace("({})", '')
            strDisplayedPrompt = strPromptFormat.format(
                strPrompt, pvDefault. ListUtilities.FormatEltsSeparatedBy(
                    '/', choiceValueSet))
            theResult = input(strDisplayedPrompt)
            if inputValidator is not None:
                if not inputValidator(theResult, choiceValueSet):
                    invalidInputHandler()
                    return None
            return theResult
        except KeyboardInterrupt as e:
            raise e
    
    @staticmethod
    def PromptForString(strPrompt, strDefault, choiceValueSet=[], 
                        inputValidator=None, invalidInputHandler=None):
        try:
            theResult = Prompter.__DoDisplayPrompt(strPrompt, strDefault, 
                choiceValueSet, inputValidator, invalidInputHandler)
            if theResult is None or not len(theResult.strip()):
                theResult = strDefault
            return theResult
        except KeyboardInterrupt as e:
            raise e

    @staticmethod
    def PromptForInt(strPrompt, nDefault, strChoiceValueSet='',
                     inputValidator=None, invalidInputHandler=None):
        try:
            theResult = int(
                    Prompter.__DoDisplayPrompt(strPrompt, nDefault, 
                    strChoiceValueSet, inputValidator, invalidInputHandler)
                )
            if theResult is None:
                theResult = nDefault
            return theResult
        except KeyboardInterrupt as e:
            raise e
        except: #parse error more likely
            if invalidInputHandler is not None:
                invalidInputHandler()
        
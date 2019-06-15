#!/usr/bin/python3
from prompters.prompter import Prompter
from common.inuyasha_symbols import EXIT_FAILURE, EXIT_SUCCESS
import os

class TheApp(object):
    @staticmethod
    def IsInteger(pvValue):
        if not pvValue:
            return False
        try:
            if not len(str(pvValue).strip()):
                return False
            _ = int(pvValue)
        except:
            return False
        else:
            return True
        pass
    
    @staticmethod
    def ValidatePort(theResult, choiceValueSet):  # @UnusedVariable
        if not TheApp.IsInteger(theResult):
            return False
        return int(theResult) >= 1024 and int(theResult) <= 49151
    import sys

    @staticmethod
    def Foo():
        print("In foo")

    @staticmethod
    def ExitInstance(message, nExitCode, exitRoutine=None):
        print(message)
        print("\nBlaaaaarrrrgggghhhh!!!! I'm dead! *plop*")
        if exitRoutine is not None:
            exitRoutine()
        os._exit(nExitCode)
        pass    
        
    @staticmethod
    def HandleInvalidPort(nPort):
        if not TheApp.IsInteger(nPort):
            print("ERROR: Must enter a number.")
            return
        print("The port", nPort, "is invalid. Range: [1024-49151].  Try again.")
        pass   
    
    @staticmethod
    def main():
#         theName = Prompter.PromptForString(strPrompt="Enter your name", 
#             strDefault="Brian", choiceValueSet=['Suzy', 'Bob', 'Greg', 'Brian'],
#             keyboardInterruptHandler=TheApp.ExitInstance)
#         print("Entered name:", theName)
        
#         nPort = 0
#         while nPort == 0:
#             nPort = Prompter.PromptForInt(strPrompt="Server's port",
#                 nDefault=9000, keyboardInterruptHandler=TheApp.ExitInstance,
#                 inputValidator=TheApp.ValidatePort, 
#                 invalidInputHandler=TheApp.HandleInvalidPort,
#                 nInvalidValue=0)
#         print("Entered port:", nPort)
        
#         shouldSave = Prompter.YesNoPrompt(strPrompt="Do you want to save?",
#             bDefault=True, keyboardInterruptHandler=TheApp.ExitInstance,
#             pvInvalidInput='<invalid input>')
#         if shouldSave:
#             print("Saving the file...")
#         else:
#             print("Save operation cancelled.")
        
#         choice = Prompter.PromptForInt(strPrompt="Menu choice", 
#             nDefault=None, choiceValueSet=[1,2,3,4],
#                  keyboardInterruptHandler=TheApp.ExitInstance)
#         print("The user chose choice:", choice)

        Prompter.PressAnyKeyToContinue(
            strPrompt="Press ENTER key to continue",
            keyboardInterruptHandler=lambda: TheApp.ExitInstance("\nyay", EXIT_SUCCESS,
                                                                 exitRoutine=TheApp.Foo))
        
        pass
    
    
if __name__ == "__main__":
    TheApp.main()

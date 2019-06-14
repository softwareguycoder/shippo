#!/usr/bin/python3
from prompters.prompter import Prompter

def main():
    theName = Prompter.PromptForString(strPrompt="Enter your name", 
        strDefault="Brian", choiceValueSet=['Suzy', 'Bob', 'Greg', 'Brian'])
    print("Entered name:", theName)
    pass
    
if __name__ == "__main__":
    main()

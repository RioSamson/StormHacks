# The journal part of the app
from operator import length_hint
from typing_extensions import Self
from webbrowser import get

class Journal: 
    #numOfEntries = 0
    def journal():
        print("Welcome to the journal!")
        print("Here, you can freely write about what you are feeling or what you are thinking about.")
        print("Anything that comes to mind and your cat buddy will quietly listen to what you have to say.")
        userInput = input("Type in whatever is on your mind, or, if don't want to say anything, just type 'pass'.\n")
        userInput = userInput.lower()
        lengthOfInput = len(userInput)

        if (userInput == "pass"):
            print("It's okay if you have nothing to share, you can always come back when you do, thank you!")
            return

        if (lengthOfInput < 100):
            print("I see, thank you for sharing")
        else:
            print("I appreciate your response. I understand it's not always easy to share this much.\nBut expressing your thoughts is always great!")


Journal.journal()

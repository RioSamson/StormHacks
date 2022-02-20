# The journal part of the app
from operator import length_hint
from webbrowser import get

class Journal: 

    numOfEntries = 1

    def journal(self):
        print("Meoww! Welcome to the journal!")
        print("ฅ^•ﻌ•^ฅ")
        print("Here, you can freely write about what you are feeling or what you are thinking about.")
        print("Anything that comes to mind and your cat buddy will quietly listen to what you have to say.")
        print("Type in whatever is on your mind, or, if don't want to say anything, just type 'pass'.\n")       
        userInput = input("Journal entry #" + str(self.numOfEntries) + ":\n")
        userInput = userInput.lower()
        lengthOfInput = len(userInput)
        if (userInput == "pass"):
            print("It's okay if you have nothing to share, you can always come back when you do, thank you!")
            return

        if (lengthOfInput < 100):
            print("I see, thank you for sharing")
        else:
            print("I appreciate your response. I understand it's not always easy to share this much.\nBut expressing your thoughts is always great!")
        self.numOfEntries += 1
from array import array

from Sleep import Sleep
from Quote import Quote

menuArray = ["Sleep", "Water", "Journal", "Emotion/Stress", "Exercise", "Exit"]
quote = Quote()

def run():
    isNotDone = True
    while(isNotDone):
        printMenu()
        userInput = int(input("Please pick from the menu (0-5) : "))
        print()
        if(userInput == 1):
            sleep = Sleep()
            sleep.run()
        if(userInput == len(menuArray)):
            print("\nThank you for using Mental Health Cat Buddy!\n")
            isNotDone = False

def printMenu():
    quoteStr = quote.getQuote()
    print("\nQuote: " + quoteStr)
    print("*********MENU*********")
    print("        ,_     _    ")
    print("        |\\_,-~/      ") 
    print("        / _  _ |    ,--.   ")
    print("       (  @  @ )   / ,-'   ")
    print("        \  _T_/-._( (     ")
    print("        /         `. \    ")
    print("       |         _  \ |   ")
    print("        \ \ ,  /      |   ")
    print("         || |-_\__   /     ")
    print("        ((_/`(____,-'     ")
    for i in range(len(menuArray)): 
        print(str (i + 1) + ") " + menuArray[i])

run()
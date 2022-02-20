from array import array

from Sleep import Sleep

menuArray = ["Sleep", "Water", "Journal", "Emotion/Stress", "Exercise", "Exit"]

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
    print("\n *********MENU*********")
    for i in range(len(menuArray)): 
        print(str (i + 1) + ") " + menuArray[i])

run()
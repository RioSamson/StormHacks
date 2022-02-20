from array import array
from statistics import median
from waterIntake import WaterIntake
from journal import Journal
from emotions import Emotions
from Exercise import Exercise
from Sleep import Sleep
from Quote import Quote
from meditation import meditation

menuArray = ["Sleep", "Water", "Journal", "Emotion/Stress", "Exercise", "Meditate", "Exit"]
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
        if (userInput == 2):
            water = WaterIntake()
            print("Would you like advice on how much water to drink? Check if you are drinking enough? Read the benefits of drinking enough water?")
            waterInput = input("Type 'advice', 'check', 'benefits', or 'quit' to leave").strip().lower()
            if (waterInput == "advice"):
                water.giveWaterAdvice()
            elif (waterInput == "check"):
                water.checkWater()
            elif (waterInput == "benefits"):
                water.listBenefits()
        if (userInput == 3):
            theJournal = Journal()
            theJournal.journal()
        if (userInput == 4):
            emotion = Emotions()

        if (userInput == 5):
            exercise = Exercise()

        if (userInput == 6):
            meditate = meditation()
            meditateLength = int(input("How long do you want to meditate? (in secs): "))
            meditate.meditate(meditateLength)
            
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

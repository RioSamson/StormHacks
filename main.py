from array import array
import os
from statistics import median
import time
from turtle import clearscreen
from waterIntake import WaterIntake
from journal import Journal
from emotions import Emotions
from Exercise import Exercise
from Sleep import Sleep
from Quote import Quote
from meditation import meditation
from socialInteraction import SocialInteraction

menuArray = ["Sleep", "Water", "Journal", "Emotion/Stress", "Exercise", "Meditate", "Social Interaction", "Exit"]
quote = Quote()

def run():
    isNotDone = True
    while(isNotDone):
        printMenu()
        userInput = int(input("Please pick from the menu (0-8) : "))
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
            emotion.getEmotion()
        if (userInput == 5):
            exercise = Exercise()
            exercise.getDailyExercise()
            exercise.summary()
        if (userInput == 6):
            meditate = meditation()
            meditate.meditate()
        if (userInput == 7):
            socialInteraction = SocialInteraction()
            socialInteraction.run()
        if(userInput == len(menuArray)):
            print("\nThank you for using Mental Health Cat Buddy!\n")
            isNotDone = False

def printMenu():
    quoteStr = quote.getQuote()
    print(quoteStr)
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

def clearScreen():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

print("Welcome to the Mental Health Cat Buddy!\nMeet Nikolai, your buddy that will accompany you through!")
print("        ,_     _    ")
print("        |\\_,-~/           meowww~") 
print("        / _  _ |    ,--.   ")
print("       (  @  @ )   / ,-'   ")
print("        \  _T_/-._( (     ")
print("        /         `. \    ")
print("       |         _  \ |   ")
print("        \ \ ,  /      |   ")
print("         || |-_\__   /     ")
print("        ((_/`(____,-'     \n\n\n")
time.sleep(5) 
clearScreen()
run()

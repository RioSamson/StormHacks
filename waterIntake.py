#ask if they are male or female or prefer not to answer
#print respective recommended amounts 
#list the benefits of staying hydrated 
#what colour is your pee 

from operator import truediv

class WaterIntake:
    def giveWaterAdvice(self):
        print("Meoww!! Welcome to the water advisor! ฅ^•ﻌ•^ฅ")
        print("To give an accurate reccommendation, choose from these options.")
        print("Are you male, female, or prefer not to answer?")
        while True:
            gender = input("Type 'male', 'female' or 'other': ").strip().lower()
            if (gender == "male"):
                print("According to The U.S. National Academies of Sciences, Engineering, and Medicine, they recommend around 12 cups of water a day!\n")
                break
            elif (gender == "female"):
                print("According to The U.S. National Academies of Sciences, Engineering, and Medicine, they recommend around 9 cups of water a day!\n")
                break
            elif (gender == "other"):
                print("That's okay if you don't want to share your gender!")
                print("According to The U.S. National Academies of Sciences, Engineering, and Medicine, they recommend around 9-12 cups of water a day!\n")
                break
            else:
                print("Oops! Sorry, please choose a valid option meow! /ᐠ .ᆺ. ᐟ\ﾉ")

    def checkWater(self):
        waterAmount = 0
        waterScore = 2
        print("Let's check your hydration levels! ฅ^•ﻌ•^ฅ Meow!")
        gender = input("Are you 'male', 'female', or prefer not to answer 'other'? ").strip().lower()
        waterAmount = int(input("On average, around how many cups a day do you drink? "))
        
        if (gender == "male"):
            if (waterAmount < 9):
                waterScore -= 1
            elif (waterAmount > 15):
                waterScore -= 1
            colourOfPee = input("What colour is your pee? 'clear', 'light yellow', or 'dark yellow'? ").strip().lower()
            if (colourOfPee == "dark yellow"):
                waterScore -= 1
            if (waterScore == 2):
                print("Meowww! You're getting the right amount of water! Great job and keep it up! /\ ___ /\ ")
                print("                                                                            (=✪ o ✪=)\n")
            elif (waterScore == 1):
                print("That's decent! A few more cups of water wouln't hurt! /ᐠ^-^ᐟ\ \n")
            elif (waterScore == 0):
                print("Seems like you need to drink more water, try having a water bottle nearby!\n")
        
        elif (gender == "female"):
            if (waterAmount < 6):
                waterScore -= 1
            elif (waterAmount > 12):
                waterScore -= 1
            colourOfPee = input("What colour is your pee? 'clear', 'light yellow', or 'dark yellow'? ").strip().lower()
            if (colourOfPee == "dark yellow"):
                waterScore -= 1
            if (waterScore == 2):
                print("Meowww! You're getting the right amount of water! Great job and keep it up! /\ ___ /\ ")
                print("                                                                            (=✪ o ✪=)\n")
            elif (waterScore == 1):
                print("That's decent! A few more cups of water wouln't hurt! /ᐠ^-^ᐟ\ \n")
            elif (waterScore == 0):
                print("Seems like you need to drink more water, try having a water bottle nearby!\n")

        elif (gender == "other"):
            if (waterAmount < 7):
                waterScore -= 1
            elif (waterAmount > 13):
                waterScore -= 1
            colourOfPee = input("What colour is your pee? 'clear', 'light yellow', or 'dark yellow'? ").strip().lower()
            if (colourOfPee == "dark yellow"):
                waterScore -= 1
            if (waterScore == 2):
                print("Meowww! You're getting the right amount of water! Great job and keep it up! /\ ___ /\ ")
                print("                                                                            (=✪ o ✪=)\n")
            elif (waterScore == 1):
                print("That's decent! A few more cups of water wouln't hurt! /ᐠ^-^ᐟ\ \n")
            elif (waterScore == 0):
                print("Seems like you need to drink more water, try having a water bottle nearby!\n")
    
    def listBenefits(self):
        print("Water is a key player in maintaining a healthy mind and body meow!")
        print("It's super important to cats like me too! I hate it when my owner forgets to leave water out for me")
        print("(=🝦 ﻌ 🝦=)")
        listOfWaterBenefits = ["Helps with delivering nutrients and oxygen to your cells",
        "Aids in digestion", "Stabilizing heartbeat", "Help with energy levels and brain function", 
        "Can help with weight loss", "And many more!"]
        print("Here are a few key benefits to drinking enough water: ")
        counter = 0
        for i in listOfWaterBenefits:
            counter += 1
            print(str(counter) + ". " + i)
        print("Try your best to drink enough water! And I'll continue to beg my owner for regular water... (=〃ﻌ〃=)")
        print

# water = WaterIntake()
# water.giveWaterAdvice()
# water.checkWater()
# water.listBenefits()

#ask if they are male or female or prefer not to answer
#print respective recommended amounts 
#list the benefits of staying hydrated 
#what colour is your pee 

class WaterIntake:
    def giveWaterInfo(self):
        print("Meoww!! Welcome to the water advisor! ฅ^•ﻌ•^ฅ")
        print("To give an accurate reccommendation, choose from these options.")
        print("Are you male, female, or prefer not to answer?")
        while True:
            gender = input("Type 'male', 'female' or 'other': ")
            gender = gender.lower().strip()
            if (gender == "male"):
                print("According to The U.S. National Academies of Sciences, Engineering, and Medicine, they recommend around 12 cups of water a day!")
                break
            elif (gender == "female"):
                print("According to The U.S. National Academies of Sciences, Engineering, and Medicine, they recommend around 9 cups of water a day!")
                break
            elif (gender == "other"):
                print("That's okay if you don't want to share your gender!")
                print("According to The U.S. National Academies of Sciences, Engineering, and Medicine, they recommend around 9-12 cups of water a day!")
                break
            else:
                print("Oops! Sorry, please choose a valid option meow! /ᐠ .ᆺ. ᐟ\ﾉ")

    def checkWater(self):
        print("Let's check your hydration levels! ฅ^•ﻌ•^ฅ Meow!")
        gender = input("Are you 'male', 'female', or prefer not to answer 'other'?")

        gender = gender.lower().strip()
        waterAmount = 0
        waterAmount = input 




water = WaterIntake()
water.giveWaterInfo()


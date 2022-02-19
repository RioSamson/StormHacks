class Sleep:

    def run(self):
        print(self)
        self.inputAge()
        print("Let's try to get some good sleep tonight!")

    def inputAge(self):
        userInput = int(input("Please type you age : "))
        if(userInput < 6):
            self.sleepInput(10, 17)
        elif(userInput <= 12):
            self.sleepInput(9, 12)
        elif(userInput <= 18):
            self.sleepInput(8, 10)
        elif(userInput <= 60):
            self.sleepInput(7, 11)
        elif(userInput <= 64):
            self.sleepInput(7, 9)
        else:
            self.sleepInput(7, 8)

    def sleepInput(self, low, high):
        userInput = int(input("How many hours of sleep did you get: "))
        if (userInput > high):
            print("You might be sleeping more than what is recommended for you!")
        elif (userInput < low):
            print("You might be sleeping less than what is recommended for you!")
        else:
            print("\nHey, nice job! You are getting the recommended amount of sleep.")
            print("             |\      _,,,---,,_           ")
            print("       ZZZzz /,`.-'`'    -.  ;-;;,_       ")
            print("            |,4-  ) )-,_. ,\ (  `'-'      ")
            print("           '---''(_/--'  `-'\_)  Felix Lee\n\n\n")

    def __str__(self):
        return "Hi! This is the sleep tracker."


ss1 = Sleep()
ss1.run()
# hours = ss1.getTimeSlept()
# print(hours)
# print(ss1)
# ss1.sleepInput()

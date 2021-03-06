class Sleep:

    def run(self):
        print(self)
        self.inputAge()
        print("Let's try to get some good sleep tonight!\n")

    def inputAge(self):
        while True:
            userInput = input("Please type you age : ")
            if userInput.isnumeric():
                break
        if(int(userInput) < 6):
            self.sleepInput(10, 17)
        elif(int(userInput) <= 12):
            self.sleepInput(9, 12)
        elif(int(userInput) <= 18):
            self.sleepInput(8, 10)
        elif(int(userInput) <= 60):
            self.sleepInput(7, 11)
        elif(int(userInput) <= 64):
            self.sleepInput(7, 9)
        else:
            self.sleepInput(7, 8)

    def sleepInput(self, low, high):
        while True:
            userInput = input("How many hours of sleep did you get: ")
            if userInput.isnumeric():
                break
        if (int(userInput) > high):
            print("You might be sleeping more than what is recommended for you!")
        elif (int(userInput) < low):
            print("You might be sleeping less than what is recommended for you!")
        else:
            print("\nHey, nice job! You are getting the recommended amount of sleep.")
            print("             |\      _,,,---,,_           ")
            print("       ZZZzz /,`.-'`'    -.  ;-;;,_       ")
            print("            |,4-  ) )-,_. ,\ (  `'-'      ")
            print("           '---''(_/--'  `-'\_)  Felix Lee\n\n\n")

    def __str__(self):
        return "Meoww! Welcome to the sleep tracker! (=^-ω-^=) "



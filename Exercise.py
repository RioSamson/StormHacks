class Exercise: 

    intensityLevels = ["light", "moderate", "intense"]
    numOfActivities = 0
    activities = []
    totalTime = 0

    def getActivity(self):
        intensity = ""
        activity = input("Activity: ")
        while True:
            intensity = input("On a scale of 1 to 3, how intense was this session? ")
            if intensity.isnumeric() and int(intensity) in range(1,4):
                break
        mins = 0
        while True:
            mins = input("How long was this session in minutes? ")
            if mins.isnumeric():
                break
        self.totalTime += int(mins)
        self.activities.append({'activity': activity, 'intensity': int(intensity)-1, 'mins': mins})

    def getDailyExercise(self):
        while True:
            self.numOfActivities = input("How many times did you exercise today? ")
            if self.numOfActivities.isnumeric():
                break
        for i in range(int(self.numOfActivities)):
            self.getActivity()

    def summary(self):
        if self.totalTime >= 45:
            print("Good job! You exercised for a total of", self.totalTime, "minutes today:")
        elif self.totalTime > 0:
            print("You exercised for", self.totalTime, "minutes today:")
        else:
            print("Don't forget to exercise tomorrow!")
        for i in range(int(self.numOfActivities)):
            print(self.activities[i]['mins'], "minutes of", self.intensityLevels[self.activities[i]['intensity']], self.activities[i]['activity'])




        
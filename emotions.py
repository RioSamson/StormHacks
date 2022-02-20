from journal import Journal

class Emotions:
    emotions = ["angry", "stressed", "sad", "happy", "excited"]

    def getEmotion(self):
        while True:
            emotion = input("How are you feeling today? (angry, stressed, sad, happy, excited) ")
            if emotion in self.emotions:
                break
        scale = self.emotions.index(emotion)
        if scale <= 2:
            if scale == 1:
                self.stressTracker()
            print("Hmmm, that's not good. Would you like to talk about it in your journal?")
            myJournal = Journal()
            myJournal.journal()
        else:
            print("Meoww! I'm so glad you are feeling", emotion, "today!")
        
    def stressTracker(self):
        while True:
            lvl = input("On a scale of 1-10, how stressed are you feeling? ")
            if int(lvl) in range(1,11):
                break

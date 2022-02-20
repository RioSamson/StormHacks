import time

class meditation:
    def meditate(self):
        while True:
            secs = input("How long do you want to meditate? (in secs): ")
            if secs.isnumeric():
                break            
        print("Purrr.. Let us do a quick meditation exercise (=^ ◡ ^=) ")
        time.sleep(2.0)
        print("As you are going through this exercise, try to clear your mind and focus on your breathing...\n")
        time.sleep(2.5)
        for i in range(int(secs)//5):
            if i != 0:
                time.sleep(5.0)
            print("Breathe in...")
            time.sleep(5.0)
            print("Breate out...")
        time.sleep(2.0)
        print("Purrr! You just meditated for", secs, "seconds.")

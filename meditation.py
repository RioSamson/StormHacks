import time

class meditation:
    def meditate(self, secs):
        for i in range(int(secs/5)):
            if i != 0:
                time.sleep(5.0)
            print("Breathe in...")
            time.sleep(5.0)
            print("Breate out...")
        time.sleep(2.0)
        print("Purrr! You just meditated for", secs, "seconds.")
        
obj = meditation()
obj.meditate(15)
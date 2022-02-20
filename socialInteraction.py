class SocialInteraction:
    def run(self):
        print(self)
        userInput = input("Did you have any social interactions today? (y/n): ")
        if(userInput == "y"):
            print("That's great! Meow")
            userInput1 = input("Was the interaction positive? (y/n): ")
            if(userInput1 == "y"):
                print("That is Amazing! (◕ᆽ◕ﾐ)ฅ\n")
            else:
                print("Awww that sucks. Keep your spirits up. Look at this cat")
                print(" Art by Marcin Glinski ")
                print("       ,")
                print("       \`-._           __")
                print("        \\  `-..____,.'  `.")
                print("         :`.         /    \`.")
                print("         :  )       :      : \ ")
                print("          ;'        '   ;  |  :")
                print("          )..      .. .:.`.;  :")
                print("         /::...  .:::...   ` ;")
                print("         ; _ '    __        /:\ ")
                print("         `:o>   /\o_>      ;:. `.")
                print("        `-`.__ ;   __..--- /:.   \ ")
                print("        === \_/   ;=====_.':.     ;")
                print("         ,/'`--'...`--....        ;")
                print("              ;                    ;")
                print("            .'                      ;")
                print("          .'                        ;")
                print("        .'     ..     ,      .       ;")
                print("       :       ::..  /      ;::.     |")
                print("      /      `.;::.  |       ;:..    ;")
                print("     :         |:.   :       ;:.    ;")
                print("     :         ::     ;:..   |.    ;")
                print("      :       :;      :::....|     |")
                print("      /\     ,/ \      ;:::::;     ;")
                print("    .:. \:..|    :     ; '.--|     ;")
                print("   ::.  :''  `-.,,;     ;'   ;     ;")
                print(".-'. _.'\      / `;      \,__:      \ ")
                print("`---'    `----'   ;      /    \,.,,,/")
                print("                   `----`              fsc")
        else:
            print("That's ok! There is always tomorrow.")
            userInput2 = int(input("How long has it been since you last interacted with someone? (in days): "))
            if(userInput2 < 3):
                print("Hey, look at you go! Meow* A social human you are.\n")
            elif(userInput2 < 20 ):
                print("Meow* We should probably talk to people you know. Give someone a call!\n")
            elif(userInput2 > 20):
                print("Meow*, do you want some help talking to someone? Here are some resources.\n")
                print("https://foundrybc.ca/get-support/phone-online-support/")

    def __str__(self):
        return "Meow! Welcome the Social Interaction Tracker. ก₍⸍⸌̣ʷ̣̫⸍̣⸌₎ค"

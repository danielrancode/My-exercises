def getLimit():
    maxStr = input()
    if not maxStr:
        print ("you didn't type anything, silly. try again.")
        getInput()
    else:
        try:
            maxInt = int(maxStr)
        except ValueError:
            print ("You are either sloppy or passive-aggressive. Try again, this time give me a whole positive number.")
            getInput()
        else:
            if maxInt < 1:
                print ("You're being a smart-ass. Keep trying.")
                maxStr = None
                getInput()
            else:
                tweet = input("What is your tweet?\n")
                while len(tweet) == 0:
                    tweet = input("You didn't type anything. Try again.\n")
                if len(tweet) > maxInt:
                    if len(tweet) - maxInt == 1:
                        print ("Your tweet is " + str(len(tweet)) + " charachters long, which is 1 charachter longer than allowed.")
                    else:
                        print ("Your tweet is " + str(len(tweet)) + " charachters long, which is " + str(len(tweet) - maxInt) + " charachters longer than allowed.")
                elif len(tweet) == maxInt:
                    if len(tweet) == 1:
                        print ("Your tweet has exactly 1 charachter, the longest possible.")
                    else:
                        print ("Your tweet has exactly " + str(len(tweet)) + " charachters, the longest possible.")
                elif len(tweet) < maxInt:
                    if maxInt - len(tweet) == 1:
                        if len(tweet) == 1:
                            print ("Your tweet is 1 charachter long. You have 1 remaining charachter to use.")
                        else:
                            print ("Your tweet is " + str(len(tweet)) + " charachters long. You have 1 remaining charachter to use.")
                    else:
                        if len(tweet) == 1:
                            print ("Your tweet is 1 charachter long. You have " + str(maxInt - len(tweet)) + " remaining charachters to use.")
                        else:
                            print ("Your tweet is " + str(len(tweet)) + " charachters long. You have " + str(maxInt - len(tweet)) + " remaining charachters to use.")

def main:
    print ("What is the maximum number of charachters allowed in a tweet?")
    getLimit()

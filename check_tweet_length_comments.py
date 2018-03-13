def getInput():
    maxStr = input()                                        # get limit from user
    if not maxStr:                                          # if user didn't type anything, reply and start over
        print ("you didn't type anything, silly. try again.")
        getInput()
    else:
        try:                                                # check if input is an integer
            maxInt = int(maxStr)
        except ValueError:                                  # if input is not an integer, reply and start over
            print ("You are either sloppy or passive-agressive. Try again, this time give me a whole positive number.")
            getInput()
        else:
            if maxInt < 1:                                  # if the number is smaller than 1, reply and start over
                print ("You're being a smart-ass. Keep trying.")
                maxStr = None
                getInput()
            else:
                tweet = input("What is your tweet?\n")      # ask for the tweet
                while len(tweet) == 0:                      # if no content, reply and ask again
                    tweet = input("You didn't type anything. Try again.\n")
                if len(tweet) > maxInt:                     # if tweet is over the limit, there are two possible replies:
                    if len(tweet) - maxInt == 1:                # reply if difference is 1 reply
                        print ("Your tweet is " + str(len(tweet)) + " charachters long, which is 1 charachter longer than allowed.")
                    else:                                       # reply if difference is bigger than 1
                        print ("Your tweet is " + str(len(tweet)) + " charachters long, which is " + str(len(tweet) - maxInt) + " charachters longer than allowed.")
                elif len(tweet) == maxInt:                  # if tweet length is exactly the maximum, two possible replies
                    if len(tweet) == 1:                         # reply if tweet is 1 character long
                        print ("Your tweet has exactly 1 one charachter, the longest possible.")
                    else:                                       # reply if tweet is longer than 1 character
                        print ("Your tweet has exactly " + str(len(tweet)) + " charachters, the longest possible.")
                elif len(tweet) < maxInt:                   # if tweet is shorter than the limit, there are four possible replies
                    if maxInt - len(tweet) == 1:                # if difference is 1:
                        if len(tweet) == 1:                         # reply if tweet length is also 1
                            print ("Your tweet is 1 charachter long. You have 1 remaining charachter to use.")
                        else:                                       # reply if tweet is longer than 1
                            print ("Your tweet is " + str(len(tweet)) + " charachters long. You have 1 remaining charachter to use.")
                    else:                                       # if difference is bigger than 1:
                        if len(tweet) == 1:                         # reply if tweet length is 1
                            print ("Your tweet is 1 charachter long. You have " + str(maxInt - len(tweet)) + " remaining charachters to use.")
                        else:                                       # reply if tweet length is bigger than 1
                            print ("Your tweet is " + str(len(tweet)) + " charachters long. You have " + str(maxInt - len(tweet)) + " remaining charachters to use.")

print ("What is the maximum number of charachters allowed in a tweet?") # opening prompt

getInput()

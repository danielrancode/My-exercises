### define getLimit function ###
def getLimit():


    # get input from user #
    userInput = input()


    # check if there is input, if no input start over #
    if userInput == '':
        print ("you didn't type anything, silly. try again.")
        getLimit()


    # check if input is an integer, if not start over #
    else:
        global Limit
        try:
            Limit = int(userInput)
        except ValueError:
            print ("You are either sloppy or passive-aggressive. Try again, this time give me a whole positive number.")
            getLimit()

    # check if input is 1 or higher, if not start over #
        else:
            if Limit < 1:
                print ("You're being a smart-ass. Keep trying.")
                getLimit()


### define getTweet function ###
def getTweet():

    # get input from user #
    tweet = input("What is your tweet?\n")

    # check if there is input, start over if not #
    while len(tweet) == 0:
        tweet = input("You didn't type anything. Try again.\n")


    # check if tweet length exceeds limit #
    if len(tweet) > Limit:

        # response if 1 charachter too long #
        if len(tweet) - Limit == 1:
            print ("Your tweet is " + str(len(tweet)) + " charachters long, which is 1 charachter longer than allowed.")

        # response if more than multiple character too long #
        else:
            print ("Your tweet is " + str(len(tweet)) + " charachters long, which is " + str(len(tweet) - Limit) + " charachters longer than allowed.")

    # check if tweet length equals limit #
    elif len(tweet) == Limit:

        # response if tweet has only 1 charachter #
        if len(tweet) == 1:
            print ("Your tweet has exactly 1 charachter, the longest possible.")

        # response if tweet is has multiple charachters #
        else:
            print ("Your tweet has exactly " + str(len(tweet)) + " charachters, the longest possible.")

    # check if tweet length is below limit #
    elif len(tweet) < Limit:

        # check if difference between tweet length and limit is one character #
        if Limit - len(tweet) == 1:

            # response if tweet has only 1 charachter #
            if len(tweet) == 1:
                print ("Your tweet is 1 charachter long. You have 1 remaining charachter to use.")

            # response if tweet is has multiple charachters #
            else:
                print ("Your tweet is " + str(len(tweet)) + " charachters long. You have 1 remaining charachter to use.")

            # response if difference is higher than 1 AND tweet has only 1 charachter #
        else:
            if len(tweet) == 1:
                print ("Your tweet is 1 charachter long. You have " + str(Limit - len(tweet)) + " remaining charachters to use.")

            # response if difference is higher than 1 AND tweet has multiple charachters#
            else:
                print ("Your tweet is " + str(len(tweet)) + " charachters long. You have " + str(Limit - len(tweet)) + " remaining charachters to use.")

def main():
    print ("What is the maximum number of charachters allowed in a tweet?")
    getLimit()
    getTweet()

main()

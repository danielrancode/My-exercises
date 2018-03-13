import random

while True:

    num = random.randrange(1,11)

    print ("Enter a number between 1 and 10: ", end='')
    while True:
        try:
            guess = int(input())
        except ValueError:
            print ("error, try again.")
            continue
        if (guess > num):
            print ("wrong, the number is lower")
        elif (guess < num):
            print ("wrong, the number is higher")
        else:
            print ("you guessed correctly!")
            break

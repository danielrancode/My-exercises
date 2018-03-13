import random

while True:

    guess = 11
    num = random.randrange(1,11)

    print ("Enter a number between 1 and 10: ", end='')

    while (num != guess):
        try:
            guess = int(input())
        except ValueError:
            print ("error, try again.")
            continue
        if (guess > num):
            print ("wrong, the number is lower")
        if (guess < num):
            print ("wrong, the number is higher")
    print ("you guessed correctly!")

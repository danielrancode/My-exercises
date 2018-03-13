### MAIN ###
# 1. getInput - GET NUMBER FROM USER
# 2. checkIfPrime - CHECK IF NUMBER IS PRIME.
# 3. IF YES: ANNOUNCE.
# 4. IF NO: ANNOUNCE FIRST FACTOR, CONTINUE TO 5
# 5. findFactors: FIND AND ANNOUNCE ALL OTHER FACTORS

def main():
    getInput()
    checkIfPrime(num)

    if num == 0:
        print ("\n0 is not a prime number.\nTry again...")

    elif Factor <= 1:
        print ("\n", num, "is a prime number!\n\nTry again...")

    else:
        print ("\n", num, "is not a prime number.  It can be divided by", Factor, end='')

        findFactors(num, Factor)

        print ("\nTry again...")


### GET NUMBER FROM USER ###

def getInput():
    global num
    try:
        num = int(input("\nEnter a number: "))
    except ValueError:
        print ("\nInvalid Input. Try again.")
        getInput()


### CHECK IF NUMBER IS PRIME ###

def checkIfPrime(num):
    global Factor
    if num < 0:
        Factor = (-1 * num) - 1
    else:
        Factor = num - 1

    while Factor > 1:
        if num % Factor == 0:
            break
        else:
            Factor -=1


### FIND AND ANNOUNCE ALL OTHER FACTORS ###

def findFactors(num, Factor):

    while Factor > 1:
        Factor -=1
        if num % Factor == 0:
            print (",", Factor, end='')
    print (".")


###################

while True:
    main()

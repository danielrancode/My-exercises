def main ():

    global primes
    primes = [2]

    global num
    num = 2

    global PrimesWhichAddUpToPrime
    PrimesWhichAddUpToPrime = []

    global sumLimit
    sumLimit = int(input("\n\nEnter Sum-limit: "))

    longest(num, sumLimit)
    print ("****** Longest is ", PrimesWhichAddUpToPrime, " containing", len(PrimesWhichAddUpToPrime), "numbers ******")
    print ("****** for which the sum is:", sum(PrimesWhichAddUpToPrime), "\n")


################################################


def longest(num, sumLimit):

    global primes

    while primes:
        findPrimesAndSum(num, sumLimit)
        if len(primes) == 1:
            del primes[0]
        else:
            num = primes[1]
            del primes [2:]
            del primes [0]


################################################


def findPrimesAndSum(num, sumLimit):
    global PrimesWhichAddUpToPrime
    while sum(primes) <= sumLimit:
        if checkIfPrime(num) == True and num != primes[0]:
            primes.append(num)
            if checkIfPrime(sum(primes)) == True and len(primes) > len(PrimesWhichAddUpToPrime) and sum(primes) <= sumLimit:
                PrimesWhichAddUpToPrime = primes[:]
        num += 1


################################################


def checkIfPrime(x):
    factor = 2

    while factor <= (x / 2):
        if x == 2:
            return True
        elif x % factor == 0:
            return False
        else:
            factor += 1
    return True




main()

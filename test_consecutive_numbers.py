def checkIfPrime():
    factor = 2
    prime = None

    while prime == None:
        if factor > (maybePrime / 2):
            prime = True
            print(maybePrime, "is prime.")
        elif maybePrime % factor != 0:
            factor += 1
        else:
            prime = False
            print(maybePrime, "is not prime.")


def main():
    global limit, prime, primes, maybePrime, primeOfPrimes

    limit = int(input("Enter limit: "))
#   global prime
#   global primes
#   global maybePrime
    maybePrime = 1
#   global primeOfPrimes

    if limit <= 0:
        print ("There are no positive primes equal or below", limit)
    else:
        checkIfPrime()

main()

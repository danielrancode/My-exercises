def checkMoreDividers(num, divider):
    while divider > 1:
        if num % divider == 0:
            print (",", divider, end='')
            divider -=1
            checkMoreDividers(num, divider)

        else:
            divider -= 1
            checkMoreDividers(num, divider)

        num = int(input("\nTry another number:"))
        checkIfPrime(num)

def checkIfPrime(num):
    if num < 0:
        divider = -1 * num - 1
    else:
        divider = num - 1
    while divider > 1:
        if num % divider == 0:
            print (num, " is not a prime number. It can be divided by ", divider, end='')
            checkMoreDividers(num, divider)
        else:
            divider -=1

    print (num, " is a prime number! Try another number:")

def main():
    num = int(input('Enter a number: '))
    checkIfPrime(num)
    main()


main()

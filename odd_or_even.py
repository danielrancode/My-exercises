# Define function to get number from user
def get_number():
    global num
    try:
        num = int(input("\nEnter a number: "))
    except ValueError:
        print ("\nInvalid Input. Try again.")
        get_number()

# Define function to check if number is even or odd
def check_if_even(num):
    if num % 2 == 0:
        print (num, 'is an even number.')
    else:
        print (num, 'is an odd number.')

# Define main function
def main():
    get_number()
    check_if_even(num)

# Execute main function
main()

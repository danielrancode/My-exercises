# Define function to get day from user and check whether it's a weekday or the weekend
def what_day():
    day = str(input("\nWhat day is it?\n\n"))
    if day.lower() == 'saturday' or \
        day.lower() == 'sunday':
        print("\nIt's the weekend! you can sleep in!")
    elif day.lower() == 'monday' or \
        day.lower() == 'tuesday' or \
        day.lower() == 'wednesday' or \
        day.lower() == 'thursday' or \
        day.lower() == 'friday':
        print('\nBummer, get out of bed and go to work...\n')
    else:
        print("\nTry again...", end='')
        what_day()

# Define main function
def main():
        what_day()

# Execute main function
main()

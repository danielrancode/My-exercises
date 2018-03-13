


def full_sandwiches (x, y, z):  # define function
    """determines quntity of sandwiches we can make""" # explain function

    global slice_pairs
    slice_pairs = x/2

    global sandwiches

    if (slice_pairs <= y) and (slice_pairs <= z):
        sandwiches = slice_pairs
    elif (slice_pairs > y) and (y >= z):
        sandwiches = z
    else:
        sandwiches = y
    return sandwiches

def left_overs (x, y, z):
    if y - (x/2) >= 1 and z - (x/2) >= 1:
        kind = "full"
    elif y - (x/2) >= 1 and z - (x/2) < 1:
        kind = "peanut butter"
    else:
        kind = "jelly"
    return kind

def main():
    x = int(input("How many bread slices do you have?  "))
    y = int(input("How much peanut butter do you have?  "))
    z = int(input("How much Jelly do you have?  "))

    full_sandwiches(x, y, z)

    if x % 2 == 0:
        print ("you can make ", sandwiches, " full sandwiches.")
    else:
        left_overs (x, y, z)
        print ("you can make ", sandwiches, " full sandwiches and one half a sandwich of type: ", kind)

main()

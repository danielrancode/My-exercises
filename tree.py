height = input("How tall is the tree? ")
height = int(height)
spaces = height - 1
hashes = 1

for i in range(height):
    print (" " * spaces, end='')
    print ("#" * hashes)
    spaces -=1
    hashes +=2
print (" " * (height - 1) + "#")

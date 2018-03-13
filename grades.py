numeric_grade = int(input("What is your numeric grade? "))
print ("Your grade is ", end = '')
if numeric_grade > 89:
    print ("A")
elif numeric_grade > 79:
    print ("B")
elif numeric_grade > 69:
    print ("C")
elif numeric_grade > 59:
    print ("D")
else:
    print ("F")

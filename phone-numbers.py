phone_number = input ('enter a number: ')
area_code = phone_number[0:3]
number_A = phone_number[3:6]
number_B = phone_number[6:10]
formatted_number = ('(' + area_code + ') ' + number_A + '-' + number_B)

formatted_number2 = ('({})-{}-{}'.format(area_code, number_A, number_B))

print (formatted_number)
print (formatted_number2)
print ('Your area code is: ' + area_code)

money = input ("Enter investment: ")
money = float (money)
interest = input ("Enter expected annual interest: ")
interest = float (interest)
for i in range(0,10):
    money = money * (1 + interest)
    print ("After " + str(i+1) + " years, you will have ${:.2f}".format(money))

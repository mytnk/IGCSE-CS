'''1. A company decided to give bonus of 5% to employee if his/her year of service is
more than 5 years. Ask user for their salary and year of service and print the net bonus
amount.'''

salary=int(input("enter your salary = "))
yearS=int(input("enter your year of service = "))

if yearS>5 :
    bonus=salary*5/100
    print("your bonus is",bonus+salary)

else :
    print("no bonus")

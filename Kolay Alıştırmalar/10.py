number1 = int(input("Please enter a number"))
number2= int (input("Please enter a number"))

if number1<number2:
    print(list(range(number1,number2)))
elif number1>number2:
    print(list(range(number2,number1)))
else:
    print("they are equal")
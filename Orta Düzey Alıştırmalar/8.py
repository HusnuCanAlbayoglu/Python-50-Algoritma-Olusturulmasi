num = int (input("enter a number") )
if num== sum ([i if  num % i == 0 else 0 for i in range(1,num)]):
    print(f"{num} is perfect number")
else:
    print(f"{num}is not perfect number")
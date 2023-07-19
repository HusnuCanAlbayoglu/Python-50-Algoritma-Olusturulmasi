num1= int(input("enter a first number"))
num2=int(input("enter a second number"))


i=1

while (i<=num1 and i<=num2):
    if (num1%i==0 and num2%i==0):
        grc=i
    i +=1

print(f"GRC is {grc}")
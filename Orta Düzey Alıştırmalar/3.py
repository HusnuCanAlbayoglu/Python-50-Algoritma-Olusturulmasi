x=input("Enter a value")
result=""
if x.isdigit():
    for i in x:
        if int(i)<3:
            result += str(int(i)**2)
        elif int(i)%2==1:
            result+=str(int(i)-2)
        else:
            result+=str(int(i)+1)
else:
    print("invalid input")

print(result)
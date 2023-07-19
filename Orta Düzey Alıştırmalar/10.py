y=int(input("enter a number greater 1"))

if y>1:

    count=0
    for i in range(2,y):
        if y%i==0:
            count+=1
    if count== 0:
        print(f"{y} is a prime number")
    else:
        print(f"{y} is not a prime number")
else:
    print("check and enter a number greater than 1")


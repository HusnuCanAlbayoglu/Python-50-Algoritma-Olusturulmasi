x=int(input("enter a number"))
x_list=[]
while x!=1:
    if x%2==0:
        x=x/2
    elif x%2!=0:
        x=3*x+1
    x_list.append(x)
    print(x)
    print(f"max number is{max(x_list)}")
    


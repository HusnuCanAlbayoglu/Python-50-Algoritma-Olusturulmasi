x = int(input("please enter a student and wardrop"))

locker=[0 for i in range(x)]
for i in range(x):
    for j in range(i,x,i+1):
        if locker [j]== 0:
            locker[j]==1
        elif locker[j]==1:
            locker[j]= 0
print (locker.count(i))
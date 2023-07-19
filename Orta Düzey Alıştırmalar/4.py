x=int(input("enter a number"+""))

sum_i=0
for i in range(1,x):
    if x%i==0:
        sum_i+=i

sum_j=0
for j in range(1,sum_i):
    if sum_i%j==0:
        sum_j+=j

if x==sum_j:
    print(f"{x}and{sum_i}are amicable numbers")
else:
    print(f"{x}is lonely number")
     
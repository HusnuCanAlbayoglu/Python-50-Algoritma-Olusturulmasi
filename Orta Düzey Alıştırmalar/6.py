num=input("enter a number")

len_num= len(num)
sum_= 0 

for i in num:
    sum_+=int(i)**len_num

if sum_==int(num):
    print(num,"is armstrong sayidir")
else:
    print(num,"is not armstorng")
  
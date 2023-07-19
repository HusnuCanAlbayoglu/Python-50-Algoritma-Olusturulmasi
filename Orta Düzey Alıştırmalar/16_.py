list1=[3,13,11,2,1,9,5]
list2=[]

for i in range(0,len(list1)):
    if list[i] < max(list1[i:]):
        list2.append(list1[i])
print(list2)
other = {i for i in list if i not in list2}
print(sorted(list(other),reverse=True))


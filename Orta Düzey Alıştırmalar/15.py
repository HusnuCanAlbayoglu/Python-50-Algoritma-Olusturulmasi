list1=[("john",1),("jade",2),("lisa",3),("rose",4),("loude",0)]

result=[]
for i in range(len(list1)):
    for j in list1:
        if j[1]==i:
            result.append(j)
print(result)
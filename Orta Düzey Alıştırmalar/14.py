def asc(list1):
    odd=[i for i in list1 if i%2 !=0]
    odd=sorted(odd)

    k=0
    result=[]
    for i in list1:
        if i%2:
            result.append(odd[k])
            k+=1
        else:
            result.append(i)
    return result

   

asc([5,8,6,3,4])

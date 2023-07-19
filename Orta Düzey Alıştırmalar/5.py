def num_split(num):

    count=0
    result=[]
    for i in str(abs(num))[::-1]:
        result.append(int(i)*10**count)
        count+=1

    result2=[]
    if num<0:
        for i in result[::-1]:
            result2.append(-i)
    else:
        result2= result[::-1]
    
    return result2

num_split(1453)



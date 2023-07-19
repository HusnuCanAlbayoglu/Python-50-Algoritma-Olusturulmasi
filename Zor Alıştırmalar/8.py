def nearist_point(list1,cen,k):

    result=[]
    for i in list1:
        a=((i[0]-cen[0])**2+(i[1]-cen[1])**2)**0.5
        result.append([a,i])

    return [v for k,v in sorted(result)[:k]]

nearist_point ([(1,3),(5,2),(2,4)],(4,1),2)
def target(list1,target_num):

    a=[]
    for i in list1:
        for j in list1:
    
            if i+j == target_num:
                a.append([list1.index(i),list1.index(j)])
    return a

target([2,8,9,15,5,12],17)

# Alternatif yol 

#def target(list1,target_num):
    #return[[list1.index(i),list1.index(j)] for i in list1 for j in list1 if i+j==target_num]
#target([2,8,9,15,5,12],17)
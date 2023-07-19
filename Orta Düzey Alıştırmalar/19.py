def pairs(list1):
    list_new=[]
    for i in range(len(list1)//2):
        list_new.append([list1[i],list1[-1-i]])
        if len(list1)%2==1:
            list_new.append([list1[len(list1)//2],list1[len(list1)//2]])
            return list_new

pairs([1,2,3,4,5,6,7])

    
def intertwind(list1,list2):

    return list(set([j for i in list1 for j in list2 if j in i ]))

intertwind(["old","int","age","and"],["list","random","soldier","introduction","print"])

"""alternatif yol 
def intertwind(list1,list2):

new_list=[]
for i in list2:
    for j in list1:
        if j in i and j not in new_list:
            new_list.append(j)
return new_list

intertwind(["old","int","age","and"],["list","random","soldier","introduction","print"])
"""
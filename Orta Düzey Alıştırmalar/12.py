sentence = input("Enter a sentence")

my_list=[]
for i in sentence:
    if i.isalpha():
        my_list.append(i)

result=[]
for i in range (len(my_list)):
    if (my_list[i],my_list.count(my_list[i])) not in result:
        result.append((my_list[i],my_list.count(my_list[i])))

print(result)

"""alternatif yol

sentences=input("enter a sentences")

my_dict=dict()
for i in sentences:
    if i.isalpha():
        if i in my_dict:
            my_dict[i]+=1
        else:
            my_dict[i]=1

print(my_dict)


"""
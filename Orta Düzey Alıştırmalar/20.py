def scramble (str1,str2):
    a=set(str1)
    count=0
    for i in str2:
        if i in a:
            count+=1
    if count==len(str2):
        return True
    else:
        return False
    
    scramble("datascientisentist","sedat")

    
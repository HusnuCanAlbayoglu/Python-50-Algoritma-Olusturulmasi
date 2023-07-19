word= input ("Enter a word").lower()
result=[]
for i in range(len(word)):
    result.append(word[:i]+word[i].upper()+word[i+1:])
print(result)




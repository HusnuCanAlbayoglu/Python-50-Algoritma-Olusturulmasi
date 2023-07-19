odds=[]
evens=[]

for i in range(1,51):
    if i %2 == 0:
        evens.append(i)
    else:
        odds.append(i)

print(odds)
print(evens)

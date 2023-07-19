number="1570"

cow,bull=0,0
count=0
while cow<len(number):
    guess=input("Enter a 4 digit")
    cow,bull=0,0
    for ind,i in enumerate(guess):
        if i in number:
            if ind==number.index(i):
                cow+=1
            else:
                bull+=1
    count+=1
    print(f"{guess}has {cow}cow,{bull}bull")

print(f"Congrats.Number of try :{count}")
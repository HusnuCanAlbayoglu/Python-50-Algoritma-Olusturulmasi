def match(check_list):
    bracket=[]
    garbage=[]
    for i in check_list:
        if i in ["(","[","{"]:
            bracket.append(i)
        elif i==")"and len(bracket)!=0 and bracket[-1]=="(":
            bracket.pop()
        elif  i=="]"and len(bracket)!=0 and bracket[-1]=="[":
            bracket.pop()
        elif  i=="}"and len(bracket)!=0 and bracket[-1]=="{":
            bracket.pop()
        else:
            garbage.append(i)
    print(bracket==[] and garbage==[])

match(["(","[",")","]"])


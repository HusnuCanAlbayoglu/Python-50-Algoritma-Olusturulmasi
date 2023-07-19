s = int(input("Please enter your note"))

if 0<= s<=100:
    if s>=80:
        print("A")
    elif s>= 65 :
        print("B")
    elif s>= 55:
        print("C")
    elif s>= 50:
        print("D")
    elif s>50:
        print("F")



else:
    print("invalid input")
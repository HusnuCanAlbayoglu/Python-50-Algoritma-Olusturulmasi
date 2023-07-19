def fact(x):

    mult=1
    while x>0:
        mult*=x
        x=-1
    return mult

fact(6)


def fact(x):

    mult2=1
    for i in range(x,0,-1):
        mult2*=i 
    return mult2

fact(25)
    

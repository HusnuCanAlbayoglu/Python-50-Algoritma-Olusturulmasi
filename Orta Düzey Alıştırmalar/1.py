
#for döngüsü ile tara range in içine 1 ile 50 arası sayları sırala 
#if koşulunu kullanarak 3 ün katlarını bing, 7 nin katlarını bang ile ,hem 3 hem 7 nin katlarını bigbang ile eşitle ve print et 



for i in range(1,51):
    if i%3==0 and i%7==0:
        print("BigBang")
    elif i%3==0:
        print("Bing")
    elif i%7==0:
        print("Bang")
    else:
        print(i)


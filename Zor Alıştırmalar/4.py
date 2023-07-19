word= input("enter a sentences or word")

def crypto(word):
    alphabet="abcçdefgğhıijklmnoöprsştuüvyz"
    rot_7   ="fgğhıijklmnoöprsştuüvyzabcçde"
    new=""
    for i in word:
        if i.isupper():
            new+=(rot_7[alphabet.index(i.islower())]).upper()
        elif i.islower():
            new+=rot_7[alphabet.index(i)]
        else:
            return new
        
        crypto(word)
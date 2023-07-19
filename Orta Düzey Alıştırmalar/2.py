
kelime =input("Kelime girin")
kalin_ünlü= 0
ince_ünlü= 0
for i in kelime:
    if i in "aıou":
        kalin_ünlü+=1
    elif i in "eiöü":
        ince_ünlü+=1

print(f"kalin ünlü sayiniz{kalin_ünlü}")
print(f"ince_ünlü sayiyiniz{ince_ünlü}")
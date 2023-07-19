sentence=input("Enter a sentence")

edit_sentence= "".join(i.lower() for i in sentence if i.isalpha())

if edit_sentence==edit_sentence[::-1]:
    print(f"{sentence}is polindrom")
else:
    print(f"{sentence} is not polindrom")




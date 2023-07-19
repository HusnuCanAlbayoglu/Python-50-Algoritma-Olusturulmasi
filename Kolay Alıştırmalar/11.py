word = input("bir metin giriniz")
word_new = word.replace(word[0],"?")[1:]
print(word_new)
print(word[0],word_new)

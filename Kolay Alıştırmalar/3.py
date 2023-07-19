
company= input("Bir firma ismi giriniz:")

if len(company)>= 3:
    print(company[:3]+company[-3:])
else:
    print("emty string")
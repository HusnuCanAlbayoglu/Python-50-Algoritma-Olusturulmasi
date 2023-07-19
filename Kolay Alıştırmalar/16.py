given_str = "My phone number is (111) 222-33-44 "

output=""

for i in given_str:
    if i.isnumeric():
        output += i

print(output)


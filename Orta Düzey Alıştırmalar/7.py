import random
random_num = random.randint(0,99)
guess_count=0
while True:

    guess=int(input("Enter a number 0 to 99"))
    if guess < random_num:
        print("Enter a higher number")
        guess_count+=1
    elif guess> random_num:
        print("Enter a lowest number")
        guess_count+=1
    else:
        print("Congrat")
        break

print(guess_count)
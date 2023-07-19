w = int(input("please enter your weight in kg"))
h = int(input("please enter your height in cm "))

result = round (w / ((h/100) ** 2),2)

if result < 18.5 :
    body="underweight"
elif result< 25 :
    body="normal"
elif result<30:
    body="overweight"
elif result <35:
    body="obese"

print (f"your bmi is {result} and your body type is {body}")
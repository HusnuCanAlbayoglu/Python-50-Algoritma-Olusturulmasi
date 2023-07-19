work_hour= int(input("enter your weekly  working hour"))
hourly_wage= int(input("enter your hourly wage"))

if work_hour >40:
    weakly_wage= (work_hour-40)*(1.5*hourly_wage)+40*hourly_wage
else:
    weakly_wage= work_hour*hourly_wage

print(f"your weakly wage is {weakly_wage}")
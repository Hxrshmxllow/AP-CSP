import re

letters = re.compile("[a-zA-Z]")
specialcharacters = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
numbers = re.compile("[0-9]")

p = input("What is the principle amount? $")
while letters.search(p) is True or specialcharacters.search(p) and numbers.search(p) is not True and float(p) < 0.00 and float(p) != 0.00:
    p = input("What is the principle amount? $")
r = 0.00
n = 365
t = float(input("Enter time (in years): "))
creditscore = input("What is your credit score: ")
while letters.search(creditscore) is True or specialcharacters.search(creditscore) and numbers.search(creditscore) is not True and (int(creditscore) <= 0 or int(creditscore) > 850):
    creditscore = input("What is your credit score: ")

if int(creditscore) < 300:
    r = 0.1
elif int(creditscore) <= 500:
    r = 0.08
elif int(creditscore) < 700:
    r = 0.075
elif int(creditscore) >= 800:
    if int(creditscore) == 850:
        r = 0.06
    elif int(creditscore) < 850:
        r = 0.065

a = round((float(p) * pow((1 + (r/n)), n*t)), 2)
print("$" + str(a))

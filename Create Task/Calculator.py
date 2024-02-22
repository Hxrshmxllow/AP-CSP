import re

numbers = []
actions = []
numberregex = r'[0-9]'

equation = input("Enter the equation you want to solve: ")

for number in equation.split(" "):
    if number.isdigit():
        numbers.append(int(number))

action = re.sub(numberregex, "", equation).replace(" ", "")
for x in action:
    actions.append(x)

answer = 0
while len(numbers) != 1:
    while len(actions) != 0:
        if actions[0] == "+":
            answer = numbers[0] + numbers[1]
        elif actions[0] == "-":
            answer = numbers[0] - numbers[1]
        elif actions[0] == "/":
            answer = numbers[0] / numbers[1]
        elif actions[0] == "*":
            answer = numbers[0] * numbers[1]
        actions.pop(0)
        numbers.pop(0)
        if len(numbers) != 1:
            numbers[0] = answer

print(f"Answer: {answer}")
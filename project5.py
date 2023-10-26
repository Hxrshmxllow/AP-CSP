import random

def main():
    value1 = function1()
    value2 = function2()
    function3(value1)
    function4(value2)
    function5(value1, value2)


def function1():
    value = 0
    for i in range(5):
        while True:
            try:
                value += int(input("Enter Value " + str(i+1) + ": "))
                break
            except ValueError:
                print("Please enter a numeric integer value.")
    print("The total of the 5 numbers entered is " + str(value) + ".")
    return value

def function2():
    value = 0
    for i in range(5):
        value += random.randint(1, 100)
    print("The total of the 5 numbers generated is " + str(value) + ".")
    return value

def function3(value):
    if value % 2 == 0:
        print("The total value produced from function 1 is an even number.")
    else:
        print("The total value produced from function 1 is a odd number.")
    return

def function4(value):
    if value <= 30:
        print("The total value produced from function 2 is less than or equal to 30.")
    else:
        print("The total value produced from function 2 is greater than 30.")
    return

def function5(value1, value2):
    if value1 > value2:
        print("The user-inputted value of " + str(value1) + " from function 1 is greater than the auto generated value of " + str(value2) + ".")
    else:
        print("The user-inputted value of " + str(value1) + " from function 1 is less than the auto generated value of " + str(value2) + ".")
    return

if __name__ == "__main__":
    main()

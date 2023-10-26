def printShape(number):
    row = ""
    column = number
    for i in range(number):
        for j in range(column):
            row += "*"
        print(row)
        row = ""
        column -= 1
    rerun = ""
    while "y" and "n" not in rerun:
        rerun  = input("Do you want to rerun (y/n)? ")
        if "y" in rerun:
            askForInput()  

def askForInput():
    while True:
        try:
            number  = int(input("Enter a numeric value: "))
            printShape(number)
        except ValueError:
            print("Please enter a numeric value.")
            
askForInput()

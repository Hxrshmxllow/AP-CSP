def getVariables():
    while True:
        try:
            numerator = int(input("Enter a numerator: "))
            denominator = int(input("Enter a denominator: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    divide(numerator, denominator)

def divide(numerator, denominator):
    if denominator == 0:
        getVariables()
    remainder = (numerator % denominator)
    mixednum = int((numerator - remainder) / denominator)
    print(str(numerator) + " / " + str(denominator) + " is an improper fraction and its mixed fraction is " + str(mixednum) + " + " + str(remainder) + "/" + str(denominator))

getVariables()
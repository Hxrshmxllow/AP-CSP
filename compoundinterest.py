p = float(input("Enter a principle amount: $"))
r = 0.03875
n = 365
t = float(input("Enter time (in years): "))
a = round((p * pow((1 + (r/n)), n*t)), 2)
print("$" + str(a))
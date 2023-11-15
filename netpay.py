from client import *

def main():
    overtimehours = 0
    while True:
        try:
            hours = int(input("Number of hours worked (0-50): "))
            if hours > 50 or hours < 0:
                print("Please enter a number between 0 and 50")
            elif hours > 40:
                overtimehours = hours - 40
                hours = 40
                break
            else:
                break
        except ValueError:
            print("Please enter a number between 0 and 50")

    federaltax = 0.014
    njtax = 0.10
    healthcare = 212 # $424 monthly so $212 for half month or bi weekly
    investment = 50
    hourlypay = 15
    overtimepay = 15 * 1.5

    grosspay = (hours * hourlypay) + (overtimehours * overtimepay)
    benefits = healthcare + investment
    netpay = (grosspay - benefits) * (1 - (federaltax + njtax))

    print("Overtime: " + str(overtimehours) + " Hours")
    print("Overtime Pay: " + str(overtimehours * overtimepay))
    print("Gross Pay Before Benefits: " + str(grosspay))
    print("Gross Pay After Benefits: " + str(grosspay - benefits))
    print("Net Pay: " + str(netpay))



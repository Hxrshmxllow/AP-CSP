from client import *

overtimehours = 0
hours = 0
overtimehours = 0
federaltax = 0.014
njtax = 0.10
healthcare = 212 # $424 monthly so $212 for half month or bi weekly
investment = 50
hourlypay = 0.00
overtimepay = 15 * 1.5
overtime = 0.00
grosspay = 0.00
benefits = 0.00
taxes = 0.00
netpay = 0.00

def printinfo():
    print("Overtime: " + str(overtimehours) + " Hours")
    print("Overtime Pay: " + str(overtime))
    print("Gross Pay Before Benefits: " + str(grosspay))
    print("Gross Pay After Benefits: " + str(grosspay - benefits))
    print("Net Pay: " + str(netpay))


def get_input():
    while True:
        try:
            hours = int(input("Number of hours worked (0-50): "))
            if get_hours_worked(hours):
                break
        except ValueError:
            print("Please enter a number between 0 and 50")
    get_hourly_rate()


def get_hours_worked(hours):
    if hours > 50 or hours < 0:
        print("Please enter a number between 0 and 50")
    elif hours > 40:
        overtimehours = hours - 40
        hours = 40
        return True
    else:
        return True

def get_hourly_rate():
    while True:
        try:
            hourlypay = float(input("Hourly Pay: $"))
        except ValueError:
            print("Please enter a numerical value.")

def calc_gross_pay():
    grosspay = (hours * hourlypay) + (overtimehours * overtimepay)

def calc_overtime():
    overtime = overtimehours * overtimepay

def calc_withholdings():
    calc_taxes()
    calc_benefits()

def calc_taxes():
    taxes = 1 - (federaltax + njtax)

def calc_benefits():
    benefits = healthcare + investment

def calc_net_pay():
    netpay = (grosspay - benefits) * taxes
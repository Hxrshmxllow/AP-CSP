employeeName = input("Enter employee Name: ")
hours = float(input("Enter number of hours worked in a week: "))
payrate = float(input("Enter hourly pay rate: $"))
federalTaxRate = float(input("Enter federal tax witholding rate: "))
stateTaxRate = float(input("Enter state tax witholding rate: "))
overtime = 0.0
if(hours > 40):
    overtime = float(hours - 40)
overtimepay = float(overtime * (payrate*1.5))
grosspay = (hours * payrate) + overtimepay
federalTaxPercent = format(federalTaxRate, ".0%")
stateTaxPercent = format(stateTaxRate, ".0%")
federalpayment = grosspay * federalTaxRate
statepayment = grosspay * stateTaxRate
netpay = grosspay - federalpayment - statepayment


print("Employee Name: " + employeeName)
print("Hours Worked: " + str(hours))
print("Pay Rate: $" + str(payrate))
if(hours > 40):
    print("Overtime Hours: " + str(overtime))
    print("Overtime Pay: $" + str(round(overtimepay, 2)))
print("Gross Pay: $" + str(round(grosspay, 2)))
print("Deductions:")
print("     Federal Witholding (" + str(federalTaxPercent) + "): $" + str(round(federalpayment, 2)))
print("     State Witholding (" + str(stateTaxPercent) + "): $" + str(round(statepayment, 2)))
print("     Total Deductions: $" + str(round((statepayment + federalpayment), 2)))
print("Net Pay: $" + str(round(netpay, 2)))



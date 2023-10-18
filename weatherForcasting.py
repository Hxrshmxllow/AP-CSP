def probablility(pA):
    if 0.8 <= pA <= 1:
        return "high"
    elif 0.6 <= pA <= 0.79:
        return "medium"
    elif 0.4 <= pA <= 59:
        return "low"
    else:
        return "no chance"

def condition(totaRainFall):
    if totalRainFall > 15:
        print("Reservoir is now at 80% Capacity.")
    else:
        print("We are still in drought conditions.")

rainfall = []
dryDays = 0
totalRainFall = 0
for i in range(5):
    rain = float(input("What was the rainfall on day " + str(i+1) + ": "))
    totalRainFall += rain
    if rain == 0:
        dryDays += 1
    rainfall.append(rain)

pA = (5 - dryDays) / 5
print("The probablility of rain of tomorrow is " + probablility(pA) + " with a " + str(format(pA, "0.0%")) + " chance of rain.")
condition(totalRainFall)

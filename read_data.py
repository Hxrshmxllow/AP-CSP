data = open("data.txt", "r")
datalist = []
for line in data:
    list = []
    for number in line.split(" "):
        list.append(int(number.replace("\n", "")))
    datalist.append(list)

rowavg = []
columnsum = []
total = 0
max = 0

for row in datalist:
    sum = 0
    count = 0
    for number in row:
        if number > max:
            max = number
        sum += number
        count += 1
        total += 1
    rowavg.append(sum/count)

print(f"Total number of values: {total}")

print("\nAverage value of each row:")
for i in range(len(rowavg)):
    print(f"Row {i+1}: {rowavg[i]}")

for column in range(len(datalist[0])):
    sum = 0
    for row in range(len(datalist)):
        sum += datalist[row][column]
        count += 1
    columnsum.append(sum)

print("\nSum of each column:")
for i in range(len(columnsum)):
    print(f"Column {i+1}: {columnsum[i]}")

print(f"\nMaximum value in the dataset: {max}")


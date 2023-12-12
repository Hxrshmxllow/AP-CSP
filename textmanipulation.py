data = open("original_data.txt", "r")
datalist = []
for line in data:
    list = []
    for number in line.split(","):
        list.append(number.replace("\n", ""))
    datalist.append(list)
x = 1
for list in datalist:
    list.sort()
    total = 0
    for number in list:
        total += int(number)
    avg = total/len(list)
    min = list[0]
    max = list[len(list)-1]
    list.append(min)
    list.append(max)
    print("Line " + str(x) + " Average: " + str(avg))
    print("Line " + str(x) + " Minimum: " + str(min))
    print("Line " + str(x) + " Maximum: " + str(max))
    x += 1

newfile = open("new_data.txt", "a")  
for list in datalist:
    count = 1
    for number in list:
        if count == len(list):
            newfile.write(str(number))
        else:
             newfile.write(str(number) + ",")
             count += 1
    newfile.write("\n")
newfile.close()    
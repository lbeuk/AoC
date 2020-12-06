with open("data.txt", "r") as data:
    sum = 0
    grouplist = []
    for line in data:
        line = line.strip()
        if line == "":
            sum += len(grouplist)
            grouplist = []
        else:
            for char in line:
                if char not in grouplist:
                    grouplist.append(char)
    print(sum)
import string

with open("data.txt", "r") as data:
    sum = 0
    grouplist = list(string.ascii_lowercase)
    for line in data:
        line = line.strip()
        if line == "":
            sum += len(grouplist)
            grouplist = list(string.ascii_lowercase)
        else:
            newgrouplist = []
            for char in grouplist:
                if char in line:
                    newgrouplist.append(char)
            grouplist = newgrouplist
    print(sum)
with open("data.txt", "r") as data:
    list = []
    for line in data:
        line = line.strip()
        binstring = ""
        for char in line:
            if char in ['F', 'L']:
                binstring += "0"
            else:
                binstring += "1"
        asint = int(binstring, 2)
        list.append(asint)
    for i in list:
        if (i+2) in list and (i+1) not in list:
            print(i+1)
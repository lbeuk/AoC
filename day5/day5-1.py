with open("data.txt", "r") as data:
    highest = 0
    for line in data:
        line = line.strip()
        binstring = ""
        for char in line:
            if char in ['F', 'L']:
                binstring += "0"
            else:
                binstring += "1"
        asint = int(binstring, 2)
        if asint > highest:
            highest = asint
    print(highest)

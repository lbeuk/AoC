with open("data.txt", "r") as data:
    good_passwords = 0
    for line in data:
        split_1 = line.split(":")
        password = split_1[1].strip()
        split_2 = split_1[0].split(" ")
        letter = split_2[1]
        split_3 = split_2[0].split("-")
        lower = int(split_3[0])
        upper = int(split_3[1])
        count = 0
        for c in password:
            if c == letter:
                count += 1
        if not (count < lower or count > upper):
            good_passwords += 1
    print(good_passwords)
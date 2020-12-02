with open("data.txt", "r") as data:
    good_passwords = 0
    for line in data:
        split_1 = line.split(":")
        password = split_1[1].strip()
        split_2 = split_1[0].split(" ")
        letter = split_2[1]
        split_3 = split_2[0].split("-")
        c1 = password[int(split_3[0]) - 1]
        c2 = password[int(split_3[1]) - 1]
        count = 0
        if (c1 == letter or c2 == letter) and not (c1 == c2): 
            good_passwords += 1
    print(good_passwords)
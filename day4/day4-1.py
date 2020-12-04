with open("data.txt", "r") as data:
    good = 0
    cur_passport = {}
    for line in data:
        if line.strip() == "":
            keys = cur_passport.keys()
            if keys.__contains__("byr") and keys.__contains__("iyr") and keys.__contains__("eyr") and keys.__contains__("hgt") and keys.__contains__("hcl") and keys.__contains__("ecl") and keys.__contains__("pid"):
                good += 1
            cur_passport = {}
        else:
            kvp = line.split(" ")
            for pair in kvp:
                split_pair = pair.split(":")
                cur_passport[split_pair[0]] = split_pair[1]
    print(good)
                
        

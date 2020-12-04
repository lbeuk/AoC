with open("data.txt", "r", encoding="utf-8") as data:
    good = 0
    cur_passport = {}
    for line in data:
        if line.strip() == "":
            keys = cur_passport.keys()
            if keys.__contains__("byr") and keys.__contains__("iyr") and keys.__contains__("eyr") and keys.__contains__("hgt") and keys.__contains__("hcl") and keys.__contains__("ecl") and keys.__contains__("pid"):
                try:
                    pv = 0

                    byr = cur_passport["byr"].strip()
                    byr_len = len(byr)
                    byr_int = int(byr)
                    if byr_len == 4:
                        if byr_int <= 2002 and byr_int >= 1920:
                            pv += 1

                    iyr = cur_passport["iyr"].strip()
                    iyr_len = len(iyr)
                    iyr_int = int(iyr)
                    if iyr_len == 4:
                        if iyr_int <= 2020 and iyr_int >= 2010:
                            pv += 1
                    
                    eyr = cur_passport["eyr"].strip()
                    eyr_len = len(eyr)
                    eyr_int = int(eyr)
                    if eyr_len == 4:
                        if eyr_int <= 2030 and eyr_int >= 2020:
                            pv += 1

                    hgt = cur_passport["hgt"].strip()
                    hgt_suf = hgt[-2:]
                    hgt_num = int(hgt [:-2])
                    if hgt_suf == "cm" and hgt_num <= 193 and hgt_num >= 150:
                        pv += 1
                    elif hgt_suf == "in" and hgt_num <= 76 and hgt_num >= 59:
                        pv += 1

                    hcl = cur_passport["hcl"].strip()
                    if len(hcl) == 7:
                        if hcl[0] == "#":
                            add = True
                            for char in hcl[1:]:
                                if char not in '1234567890abcdef':
                                    add = False
                                    print(char)
                            if add:
                                pv += 1

                    ecl = cur_passport["ecl"].strip()
                    if ecl in ["amb","blu","brn","gry","grn","hzl","oth"]:
                        pv += 1

                    pid = cur_passport["pid"].strip()
                    if len(pid) == 9:
                        pid_int = int(pid)
                        pv += 1

                    if pv == 7:
                        good += 1


                except:
                    print(cur_passport)
            cur_passport = {}
        else:
            kvp = line.split(" ")
            for pair in kvp:
                split_pair = pair.split(":")
                cur_passport[split_pair[0]] = split_pair[1]
    print(good)
                
        

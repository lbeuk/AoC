with open("data.txt", "r") as data:
    data_list = []
    for line in data:
        line_as_int = int(line)
        data_list.append(line_as_int)
    for num1 in data_list:
        for num2 in data_list:
                if num1 + num2 == 2020:
                    print(num1, " * ", num2, " = ", (num1 * num2))


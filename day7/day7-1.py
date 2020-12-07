color_to_find = "shiny gold"

def check_color(d: dict, to_find: str, in_key: str):
    for color in d[in_key]:
        if color == to_find or check_color(d, to_find, color) > 0:
            return 1
    return 0

with open("data.txt", "r") as data:
    data_as_dict = {}
    for line in data:
        cleaned_line = line.strip().replace(".", "").replace(" bags", "").replace(" bag", "").replace(" contain", ",").split(",")
        line_parent_color = cleaned_line.pop(0)
        data_as_dict[line_parent_color] = []
        for item in cleaned_line:
            item_color = item.strip()
            if "other" not in item_color:
                item_color = item_color[item_color.index(" ") + 1:]
                data_as_dict[line_parent_color].append(item_color)
    sum = 0
    for key in data_as_dict.keys():
        sum += check_color(data_as_dict, color_to_find, key)
    print(sum)




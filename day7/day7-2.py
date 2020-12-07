color_to_count_for = "shiny gold"

def count_bags(d: dict, count_for: str):
    count = 0
    for color in d[count_for]:
        color_count = color["count"]
        count += color_count * (1 + count_bags(d, color["color"]))
    return count

with open("data.txt", "r") as data:
    data_as_dict = {}
    for line in data:
        cleaned_line = line.strip().replace(".", "").replace(" bags", "").replace(" bag", "").replace(" contain", ",").split(",")
        line_parent_color = cleaned_line.pop(0)
        data_as_dict[line_parent_color] = []
        for item in cleaned_line:
            item_color = item.strip()
            if "other" not in item_color:
                split_index = item_color.index(" ")
                item_count = int(item_color[:split_index])
                item_color = item_color[split_index + 1:]
                data_as_dict[line_parent_color].append({"color": item_color, "count": item_count})
   
    print(count_bags(data_as_dict, color_to_count_for))



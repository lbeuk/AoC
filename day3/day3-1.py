x_inc = 3
y_inc = 1

with open("data.txt", "r") as data:
    lines = data.readlines()
    width = len(lines[0].strip())
    posx = 0
    posy = 0
    tree_count = 0
    while posy < len(lines) - 1:
        posx += x_inc
        posx %= width
        posy += y_inc

        if lines[posy][posx] == "#":
            tree_count += 1
    print(tree_count)
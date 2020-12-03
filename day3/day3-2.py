def get_trees(x_inc, y_inc):
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
        return tree_count

print(get_trees(1,1) * get_trees(3,1) * get_trees(5,1) * get_trees(7,1) * get_trees(1,2))
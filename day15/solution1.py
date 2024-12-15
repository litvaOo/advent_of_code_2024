map = []
position = []
moves = []
with open("input.txt") as f:
    # with open("input_test.txt") as f:
    i = 0
    is_map = True
    for line in f.readlines():
        if line == "\n":
            is_map = False
        if is_map:
            map.append(list(line.strip()))
            for j, char in enumerate(line):
                if char == "@":
                    position = [i, j]
                    map[i][j] = "."
        else:
            moves.extend(list(line.strip()))
        i += 1


def move_boulders(x, y, direction):
    if map[x][y] == ".":
        return True
    if map[x][y] == "#":
        return False
    if direction == "^":
        if x - 1 > 0 and move_boulders(x - 1, y, direction):
            map[x - 1][y] = "O"
            map[x][y] = "."
            return True
        return False
    if direction == "v":
        if x + 1 < len(map[0]) and move_boulders(x + 1, y, direction):
            map[x + 1][y] = "O"
            map[x][y] = "."
            return True
        return False
    if direction == "<":
        if y - 1 > 0 and move_boulders(x, y - 1, direction):
            map[x][y - 1] = "O"
            map[x][y] = "."
            return True
        return False
    if direction == ">":
        if y + 1 < len(map) - 1 and move_boulders(x, y + 1, direction):
            map[x][y + 1] = "O"
            map[x][y] = "."
            return True
        return False
    assert False, "shouldn't get here"


for i, line in enumerate(map):
    for j, char in enumerate(line):
        if [i, j] == position:
            print("@", end="")
        else:
            print(char, end="")
    print()
print("___________________________________________")
print("___________________________________________")
print("___________________________________________")

for move in moves:
    i, j = position
    print(move)
    if move == "^":
        if position[0] - 1 > 0:
            if map[position[0] - 1][position[1]] == ".":
                position[0] -= 1
            elif map[position[0] - 1][position[1]] == "O":
                position[0] -= move_boulders(i - 1, j, "^")
    if move == "v":
        # import pudb
        #
        # pudb.set_trace()
        if position[0] + 1 < len(map[0]) - 1:
            if map[position[0] + 1][position[1]] == ".":
                position[0] += 1
            elif map[position[0] + 1][position[1]] == "O":
                position[0] += move_boulders(i + 1, j, "v")
    if move == "<":
        if position[1] - 1 > 0:
            if map[position[0]][position[1] - 1] == ".":
                position[1] -= 1
            elif map[position[0]][position[1] - 1] == "O":
                position[1] -= move_boulders(i, j - 1, "<")
    if move == ">":
        if position[1] + 1 < len(map) - 1:
            if map[position[0]][position[1] + 1] == ".":
                position[1] += 1
            elif map[position[0]][position[1] + 1] == "O":
                position[1] += move_boulders(i, j + 1, ">")
    # for i, line in enumerate(map):
    #     for j, char in enumerate(line):
    #         if [i, j] == position:
    #             print("@", end="")
    #         else:
    #             print(char, end="")
    #     print()
    # print()
sum = 0
for i, line in enumerate(map):
    for j, char in enumerate(line):
        if char == "O":
            sum += j + i * 100
print(sum)

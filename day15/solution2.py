map = []
position = []
moves = []
with open("input.txt") as f:
    i = 0
    is_map = True
    for line in f.readlines():
        if line == "\n":
            is_map = False
        if is_map:
            map.append([])
            for j, char in enumerate(line):
                if char == "@":
                    position = [i, j * 2]
                    map[-1].extend(["@", "."])
                if char == "#":
                    map[-1].extend(["#", "#"])
                if char == ".":
                    map[-1].extend([".", "."])
                if char == "O":
                    map[-1].extend(["[", "]"])
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


sum = 0
y, x = position
for move in moves:
    diff_x, diff_y = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}[move]
    boulders_to_move = []
    boulders_to_check = [(y, x)]
    checked = set()
    can_move = True

    while boulders_to_check:
        next_y, next_x = boulders_to_check.pop(0)
        if (next_y, next_x) in checked:
            continue

        checked.add((next_y, next_x))

        dest_x, dest_y = next_x + diff_x, next_y + diff_y

        if map[dest_y][dest_x] == "#":
            can_move = False
            break

        boulders_to_move.append((next_y, next_x, dest_y, dest_x))
        if map[dest_y][dest_x] == ".":
            continue

        boulders_to_check.append((dest_y, dest_x))
        if diff_x == 0:
            if map[dest_y][dest_x] == "[":
                boulders_to_check.append((dest_y, dest_x + 1))
            elif map[dest_y][dest_x] == "]":
                boulders_to_check.append((dest_y, dest_x - 1))

    if can_move:
        while boulders_to_move:
            next_y, next_x, dest_y, dest_x = boulders_to_move.pop()
            map[dest_y][dest_x] = map[next_y][next_x]
            map[next_y][next_x] = "."
        x, y = x + diff_x, y + diff_y


for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == "[":
            sum += j + 100 * i
print(sum)

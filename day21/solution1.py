from functools import cache
from itertools import permutations

lines = []
with open("input.txt") as f:
    for line in f:
        lines.append(line.strip())

positions_code = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}

positions_keypad = {"^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}
movements = []

diff = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0),
}


@cache
def search(line, curr, next, keypad):
    if next == len(line):
        return [""]
    curr_post = ()
    if curr == -1:
        curr_post = positions_keypad["A"] if keypad else positions_code["A"]
    else:
        curr_post = (
            positions_keypad[line[curr]] if keypad else positions_code[line[curr]]
        )
    next_pos = positions_keypad[line[next]] if keypad else positions_code[line[next]]

    movement = []
    res = set()
    if abs(curr_post[0] - next_pos[0]) > 0:
        if curr_post[0] - next_pos[0] > 0:
            movement.extend(["^"] * abs(curr_post[0] - next_pos[0]))
        else:
            movement.extend(["v"] * abs(curr_post[0] - next_pos[0]))
    if abs(curr_post[1] - next_pos[1]) > 0:
        if curr_post[1] - next_pos[1] > 0:
            movement.extend(["<"] * abs(curr_post[1] - next_pos[1]))
        else:
            movement.extend([">"] * abs(curr_post[1] - next_pos[1]))
    for option in set(permutations(movement)):
        tmp_pos = [curr_post[0], curr_post[1]]
        for char in option:
            tmp_pos[0] += diff[char][0]
            tmp_pos[1] += diff[char][1]
            if (not keypad and tmp_pos == [3, 0]) or (keypad and tmp_pos == [0, 0]):
                break
        else:
            if next + 1 == len(line):
                res.add("".join(option) + "A")
            else:
                tmp = search(line, next, next + 1, keypad)
                for new_line in tmp:
                    res.add("".join(option) + "A" + new_line)
    return res


sum = 0
for line in lines:
    res1 = search(line, -1, 0, False)
    res2 = set()
    for item in res1:
        for string in search(item, -1, 0, True):
            res2.add(string)
    res3 = set()
    for item in res2:
        for i in search(item, -1, 0, True):
            res3.add(i)
    shortest = sorted(res3, key=lambda x: len(x))[0]
    print(shortest, len(shortest))
    sum += int(line[:-1]) * len(shortest)
print(sum)

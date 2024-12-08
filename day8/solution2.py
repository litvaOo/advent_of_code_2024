from collections import defaultdict
from itertools import combinations


lines = []
hashmap = defaultdict(lambda: list())
with open("input.txt") as f:
    lines = f.readlines()

matrix = []
for line_num, line in enumerate(lines):
    matrix.append([])
    for col, char in enumerate(line):
        matrix[-1].append(ord(char))
        if char == "." or char == "\n":
            continue
        hashmap[char].append([line_num, col])

sum = 0
for key in hashmap.keys():
    for pair in combinations(hashmap[key], 2):
        x_diff = pair[1][1] - pair[0][1]
        y_diff = pair[1][0] - pair[0][0]
        position = [pair[0].copy(), pair[1].copy()]
        while (
            position[0][1] - x_diff > -1
            and position[0][1] - x_diff < len(lines[0]) - 1
            and position[0][0] - y_diff > -1
            and position[0][0] - y_diff < len(lines)
        ):
            matrix[position[0][0] - y_diff][position[0][1] - x_diff] = ord("#")
            sum += 1
            position[0][0] -= y_diff
            position[0][1] -= x_diff
        position = [pair[0].copy(), pair[1].copy()]
        while (
            position[1][1] + x_diff > -1
            and position[1][1] + x_diff < len(lines[0]) - 1
            and position[1][0] + y_diff > -1
            and position[1][0] + y_diff < len(lines)
        ):
            matrix[position[1][0] + y_diff][position[1][1] + x_diff] = ord("#")
            sum += 1
            position[1][0] += y_diff
            position[1][1] += x_diff
res = 0
for line in matrix:
    for char in line:
        if chr(char) != "." and chr(char) != "\n":
            res += 1
print(res)

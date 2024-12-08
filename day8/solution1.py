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
        if char == ".":
            continue
        hashmap[char].append([line_num, col])

print(hashmap)
sum = 0
for key in hashmap.keys():
    for pair in combinations(hashmap[key], 2):
        # print(pair)
        x_diff = pair[1][1] - pair[0][1]
        y_diff = pair[1][0] - pair[0][0]
        # print(x_diff, y_diff)
        if (
            pair[0][1] - x_diff > -1
            and pair[0][1] - x_diff < len(lines[0]) - 1
            and pair[0][0] - y_diff > -1
            and pair[0][0] - y_diff < len(lines)
        ):
            matrix[pair[0][0] - y_diff][pair[0][1] - x_diff] = ord("#")
            # print(pair[0][0] - y_diff, pair[0][1] - x_diff)
            sum += 1
        if (
            pair[1][1] + x_diff > -1
            and pair[1][1] + x_diff < len(lines[0]) - 1
            and pair[1][0] + y_diff > -1
            and pair[1][0] + y_diff < len(lines)
        ):
            matrix[pair[1][0] + y_diff][pair[1][1] + x_diff] = ord("#")
            # print(pair[1][0] + y_diff, pair[1][1] + x_diff)
            sum += 1
    # break
res = 0
for line in matrix:
    for char in line:
        if chr(char) == "#":
            res += 1
        print(chr(char), end="")
    # print()
print()
print(sum)
print(res)

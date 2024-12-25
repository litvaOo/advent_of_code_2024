keys = []
locks = []
lines = []
with open("input.txt") as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    if lines[i].strip() == "":
        i += 1
        continue
    if lines[i].strip() == ".....":
        keys.append([0] * 5)
        for j in range(1, 6):
            keys[-1][0] += lines[i + j][0] == "#"
            keys[-1][1] += lines[i + j][1] == "#"
            keys[-1][2] += lines[i + j][2] == "#"
            keys[-1][3] += lines[i + j][3] == "#"
            keys[-1][4] += lines[i + j][4] == "#"
        i += 7
    if lines[i].strip() == "#####":
        # __import__("ipdb").set_trace()
        locks.append([0] * 5)
        for j in range(1, 6):
            locks[-1][0] += lines[i + j][0] == "#"
            locks[-1][1] += lines[i + j][1] == "#"
            locks[-1][2] += lines[i + j][2] == "#"
            locks[-1][3] += lines[i + j][3] == "#"
            locks[-1][4] += lines[i + j][4] == "#"
        i += 7
sum = 0
for key in keys:
    for lock in locks:
        for i in range(5):
            if lock[i] + key[i] > 5:
                break
        else:
            sum += 1
print(sum)
# [print(line) for line in keys]
# print()
# [print(line) for line in locks]

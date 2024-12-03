import re

lines = []
with open("input.txt", "r") as file:
    lines = file.readlines()

muls = []
for line in lines:
    muls.extend(re.findall(r"mul\([0-9]*,[0-9]*\)", line))

sum = 0
for mul in muls:
    tmp = mul[4:-1].split(",")
    sum += int(tmp[0]) * int(tmp[1])

print(sum)

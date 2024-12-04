lines = []
with open("input.txt") as f:
    lines = f.readlines()

sum = 0

for j in range(len(lines)):
    line = lines[j]
    for i in range(len(line)):
        if i + 3 < len(line):
            if line[i : i + 4] == "XMAS" or line[i : i + 4] == "SAMX":
                sum += 1
            if j + 3 < len(lines):
                diagonal_right = (
                    lines[j][i]
                    + lines[j + 1][i + 1]
                    + lines[j + 2][i + 2]
                    + lines[j + 3][i + 3]
                )
                if diagonal_right == "XMAS" or diagonal_right == "SAMX":
                    sum += 1
        if j + 3 < len(lines):
            down = lines[j][i] + lines[j + 1][i] + lines[j + 2][i] + lines[j + 3][i]
            if down == "XMAS" or down == "SAMX":
                sum += 1
            if i - 3 > -1:
                diagonal_left = (
                    lines[j][i]
                    + lines[j + 1][i - 1]
                    + lines[j + 2][i - 2]
                    + lines[j + 3][i - 3]
                )
                if diagonal_left == "XMAS" or diagonal_left == "SAMX":
                    sum += 1

print(sum)

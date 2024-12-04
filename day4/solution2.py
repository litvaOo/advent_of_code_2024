lines = []
with open("input.txt") as f:
    lines = f.readlines()

sum = 0

for j in range(1, len(lines) - 1):
    line = lines[j]
    for i in range(1, len(line) - 1):
        if line[i] == "A":
            diagonal_left = (lines[j - 1][i - 1], lines[j + 1][i + 1])
            diagonal_right = (lines[j - 1][i + 1], lines[j + 1][i - 1])
            if (diagonal_right == ("M", "S") or diagonal_right == ("S", "M")) and (
                diagonal_left == ("M", "S") or diagonal_left == ("S", "M")
            ):
                sum += 1
print(sum)

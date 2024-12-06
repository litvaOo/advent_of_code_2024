lines = []
with open("input.txt") as f:
    lines = f.readlines()

matrix = []
position = [0, 0]
for line_num, line in enumerate(lines):
    matrix.append([])
    for i, c in enumerate(line):
        if c == "#":
            matrix[-1].append(-1)
        elif c == "^":
            position = [line_num, i]
        else:
            matrix[-1].append(1)

direction = [-1, 0]
sum = 0
while True:
    try:
        if position[0] + direction[0] < 0 or position[0] + direction[0] >= len(
            matrix[0]
        ):
            break
        if position[1] + direction[1] < 0 or position[0] + direction[1] >= len(matrix):
            break
        if matrix[position[0] + direction[0]][position[1] + direction[1]] == -1:
            if direction == [-1, 0]:
                direction = [0, 1]
            elif direction == [0, 1]:
                direction = [1, 0]
            elif direction == [1, 0]:
                direction = [0, -1]
            else:
                direction = [-1, 0]
        else:
            sum += matrix[position[0] + direction[0]][position[1] + direction[1]]
            position[0] += direction[0]
            position[1] += direction[1]
            matrix[position[0]][position[1]] = 0
    except IndexError:
        break
for line in matrix:
    string = ""
    for c in line:
        if c == -1:
            string += "#"
        elif c == 0:
            string += "X"
        else:
            string += "."
    print(string)
print(sum)

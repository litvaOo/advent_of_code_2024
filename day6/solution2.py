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
            matrix[-1].append(1)
        else:
            matrix[-1].append(1)

direction = [-1, 0]
points = []
start = position.copy()
sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(i, j)
        if matrix[i][j] == -1 or (i == start[0] and j == start[1]):
            continue
        matrix[i][j] = -1
        step = 0
        position = start.copy()
        direction = [-1, 0]
        while (
            step < (len(matrix) * len(matrix[0])) * 128
        ):  # I am not proud of it. But finding cycle was too long
            try:
                if position[0] + direction[0] < 0 or position[0] + direction[0] >= len(
                    matrix[0]
                ):
                    break
                elif position[1] + direction[1] < 0 or position[1] + direction[
                    1
                ] >= len(matrix):
                    break
                elif (
                    matrix[position[0] + direction[0]][position[1] + direction[1]] == -1
                ):
                    if direction == [-1, 0]:
                        direction = [0, 1]
                    elif direction == [0, 1]:
                        direction = [1, 0]
                    elif direction == [1, 0]:
                        direction = [0, -1]
                    else:
                        direction = [-1, 0]
                else:
                    position[0] += direction[0]
                    position[1] += direction[1]
                    step += 1
            except IndexError:
                break
        else:
            sum += 1
        matrix[i][j] = 1
print(sum)

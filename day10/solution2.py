lines = []
with open("input.txt") as file:
    lines = file.readlines()

matrix = []
for line in lines:
    matrix.append(list(map(int, line[:-1])))


def traverse(row, column, expected):
    if matrix[row][column] == expected:
        if expected == 9:
            return 1
        sum = 0
        if row > 0:
            sum += traverse(row - 1, column, (expected + 1))
        if row < len(matrix) - 1:
            sum += traverse(row + 1, column, (expected + 1))
        if column > 0:
            sum += traverse(row, column - 1, (expected + 1))
        if column < len(matrix[0]) - 1:
            sum += traverse(row, column + 1, (expected + 1))
        return sum
    return 0


sum = 0
for row, line in enumerate(matrix):
    for column, char in enumerate(line):
        sum += traverse(row, column, 0)
print(sum)

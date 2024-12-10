lines = []
with open("input.txt") as file:
    lines = file.readlines()

matrix = []
for line in lines:
    matrix.append(list(map(int, line[:-1])))


visited = set()


def traverse(row, column, expected):
    if matrix[row][column] == expected:
        if expected == 9:
            visited.add(",".join([str(row), str(column)]))
        if row > 0:
            traverse(row - 1, column, (expected + 1))
        if row < len(matrix) - 1:
            traverse(row + 1, column, (expected + 1))
        if column > 0:
            traverse(row, column - 1, (expected + 1))
        if column < len(matrix[0]) - 1:
            traverse(row, column + 1, (expected + 1))
        return len(visited)
    return 0


sum = 0
for row, line in enumerate(matrix):
    for column, char in enumerate(line):
        sum += traverse(row, column, 0)
        visited = set()
print(sum)

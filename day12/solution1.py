lines = []
with open("input.txt") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = list(lines[i].strip())

visited = set()


def region_search(row, col):
    perimeter = 0
    area = 1
    curr_val = lines[row][col]
    if curr_val == 0:
        return 0, 0
    visited.add(",".join([str(row), str(col)]))
    lines[row][col] = 0
    if row - 1 < 0 or lines[row - 1][col] != curr_val:
        if ",".join([str(row - 1), str(col)]) not in visited:
            perimeter += 1
    else:
        tmp = region_search(row - 1, col)
        perimeter += tmp[0]
        area += tmp[1]
    if row + 1 >= len(lines) or lines[row + 1][col] != curr_val:
        if ",".join([str(row + 1), str(col)]) not in visited:
            perimeter += 1
    else:
        tmp = region_search(row + 1, col)
        perimeter += tmp[0]
        area += tmp[1]
    if col - 1 < 0 or lines[row][col - 1] != curr_val:
        if ",".join([str(row), str(col - 1)]) not in visited:
            perimeter += 1
    else:
        tmp = region_search(row, col - 1)
        perimeter += tmp[0]
        area += tmp[1]
    if col + 1 >= len(lines[0]) or lines[row][col + 1] != curr_val:
        if ",".join([str(row), str(col + 1)]) not in visited:
            perimeter += 1
    else:
        tmp = region_search(row, col + 1)
        perimeter += tmp[0]
        area += tmp[1]
    return perimeter, area


sum = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 0:
            continue
        curr_symbol = lines[i][j]
        res = region_search(i, j)
        visited = set()
        print(curr_symbol)
        print(res[1], res[0])
        sum += res[0] * res[1]
print(sum)

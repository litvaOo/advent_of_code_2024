fills = []
lines = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        row = []
        fill_row = []
        for character in line:
            row.append(character)
            fill_row.append(" ")
        lines.append(row)
        fills.append(fill_row)


def perform_fill():
    cells = [[r, c]]
    target = lines[r][c]
    fills[r][c] = 0
    while len(cells) > 0:
        cell = cells[0]
        cells = cells[1:]
        i, j = cell[0], cell[1]
        if i - 1 >= 0 and lines[i - 1][j] == target and fills[i - 1][j] != 0:
            fills[i - 1][j] = 0
            cells.append([i - 1, j])
        if i + 1 < len(lines) and lines[i + 1][j] == target and fills[i + 1][j] != 0:
            fills[i + 1][j] = 0
            cells.append([i + 1, j])
        if j - 1 >= 0 and lines[i][j - 1] == target and fills[i][j - 1] != 0:
            fills[i][j - 1] = 0
            cells.append([i, j - 1])
        if j + 1 < len(lines[0]) and lines[i][j + 1] == target and fills[i][j + 1] != 0:
            fills[i][j + 1] = 0
            cells.append([i, j + 1])
    return


def get_area():
    area = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if fills[i][j] == 0:
                area += 1
    return area


def get_sides():
    p = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if fills[i][j] != 0:
                continue
            if i - 1 < 0 or fills[i - 1][j] != 0:
                if (
                    j - 1 < 0
                    or fills[i][j - 1] != 0
                    or (i - 1 >= 0 and fills[i - 1][j - 1] == 0)
                ):
                    p += 1
            if i + 1 >= len(lines) or fills[i + 1][j] != 0:
                if (
                    j - 1 < 0
                    or fills[i][j - 1] != 0
                    or (i + 1 < len(lines) and fills[i + 1][j - 1] == 0)
                ):
                    p += 1
            if j - 1 < 0 or fills[i][j - 1] != 0:
                if (
                    i - 1 < 0
                    or fills[i - 1][j] != 0
                    or (j - 1 >= 0 and fills[i - 1][j - 1] == 0)
                ):
                    p += 1
            if j + 1 >= len(lines[0]) or fills[i][j + 1] != 0:
                if (
                    i - 1 < 0
                    or fills[i - 1][j] != 0
                    or (j + 1 < len(lines[0]) and fills[i - 1][j + 1] == 0)
                ):
                    p += 1
    return p


def mark_fill_done():
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if fills[i][j] == 0:
                fills[i][j] = "*"
    return


total = 0
for r in range(len(lines)):
    for c in range(len(lines[0])):
        if fills[r][c] == "*":
            continue
        perform_fill()
        total += get_area() * get_sides()
        mark_fill_done()
print(total)

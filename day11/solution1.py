lines = []
with open("input.txt") as f:
    lines = f.readlines()

line = lines[0].split()
for i in range(25):
    print(i)
    skip = False
    len_line = len(line)
    j = 0
    while j < len_line:
        if skip:
            skip = False
            j += 1
            continue
        if line[j] == "0":
            line[j] = "1"
        elif len(line[j]) % 2 == 0:
            tmp = line[j]
            line[j] = line[j][: len(line[j]) // 2]
            line.insert(j + 1, str(int(tmp[len(tmp) // 2 :])))
            skip = True
            len_line += 1
        else:
            line[j] = str(int(line[j]) * 2024)
        j += 1
print(len(line))

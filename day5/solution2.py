from collections import defaultdict

lines = ""
with open("input.txt") as f:
    lines = f.readlines()
line_pointer = 0
hashmap = defaultdict(lambda: [])
while "|" in lines[line_pointer]:
    tmp = lines[line_pointer].split("|")
    hashmap[int(tmp[0])].append(int(tmp[1]))
    line_pointer += 1
line_pointer += 1

sum = 0
is_broken = False
for line in lines[line_pointer:]:
    line_processed = list(map(int, line.split(",")))

    def check_list():
        global is_broken
        for key in hashmap.keys():
            if key not in line_processed:
                continue
            for i, val in enumerate(line_processed):
                if val == key:
                    break
                if val in hashmap[key]:
                    is_broken = True
                    j = line_processed.index(key)
                    line_processed[j], line_processed[i] = (
                        line_processed[i],
                        line_processed[j],
                    )
                    return False
        return True
    tmp = False
    while not tmp:
        tmp = check_list()

    if is_broken:
        sum += line_processed[len(line_processed) // 2]
    is_broken = False
print(sum)

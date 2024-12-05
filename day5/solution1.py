from collections import defaultdict


lines = []
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
for line in lines[line_pointer:]:
    line_processed = list(map(int, line.split(",")))
    correct = True
    for key in hashmap.keys():
        if key not in line_processed:
            continue
        for i in line_processed:
            if i == key:
                break
            if i in hashmap[key]:
                correct = False
                break
    if correct:
        sum += line_processed[len(line_processed) // 2]

print(sum)

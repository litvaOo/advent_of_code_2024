from collections import defaultdict

towels = []
patterns = []
with open("input.txt") as f:
    lines = f.readlines()
    towels = sorted(lines[0].strip().split(", "), key=lambda x: len(x), reverse=True)
    for i in lines[1:]:
        if not i.strip():
            continue
        patterns.append(i.strip())


def design_possible(pattern, towels):
    todo = set()
    todo.add(pattern)
    counts = defaultdict(int, {pattern: 1})

    while len(todo) > 0:
        part = max(todo, key=len)
        todo.remove(part)
        for towel in towels:
            if part[: len(towel)] == towel:
                new_part = part[len(towel) :]
                counts[new_part] += counts[part]

                if new_part != "":
                    todo.add(new_part)

    return counts[""]


sum = 0
for pattern in patterns:
    sum += design_possible(pattern, towels)
print(sum)

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

    while len(todo) > 0:
        part = todo.pop()
        for towel in towels:
            if part[: len(towel)] == towel:
                if part == towel:
                    return True

                todo.add(part[len(towel) :])

    return False


sum = 0
for pattern in patterns:
    sum += design_possible(pattern, towels)
print(sum)

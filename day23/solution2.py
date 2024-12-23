import itertools
from collections import deque

connections = set()
computers = set()
with open("input.txt") as f:
    for line in f:
        a, b = line.strip().split("-")
        connections.add((b, a))
        connections.add((a, b))
        computers.add(a)
        computers.add(b)


todo = deque([x for x in itertools.combinations(computers, 2) if x in connections])
best = tuple()
while len(todo) > 0:
    cur = todo.popleft()
    if len(cur) > len(best):
        best = cur
    for x in computers:
        if x > cur[-1]:
            good = True
            for y in cur:
                if (x, y) not in connections:
                    good = False
                    break
            if good:
                todo.append(cur + (x,))
print(",".join(sorted(best)))

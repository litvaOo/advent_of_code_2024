from collections import defaultdict

connections = defaultdict(set)
with open("input.txt") as f:
    for line in f:
        a, b = line.strip().split("-")
        connections[a].add(b)
        connections[b].add(a)

groups = set()
for connection in connections:
    for node in connections[connection]:
        for node2 in connections[node]:
            if connection in connections[node2]:
                groups.add(frozenset([connection, node, node2]))
print(len(groups))
print("\n".join([",".join(group) for group in groups]))
sum = 0
for group in groups:
    for node in group:
        if node[0] == "t":
            sum += 1
            break
print(sum)

from collections import defaultdict

wires = defaultdict(lambda: "-1")
operations = []
with open("input.txt") as f:
    is_wires = True
    for line in f.readlines():
        if line == "\n":
            is_wires = False
            continue
        if is_wires:
            tmp = line.strip().split(":")
            wires[tmp[0]] = tmp[1]
        else:
            operations.append(line.strip())

swapped = set()


def search(wire1, wire2, operator):
    for operation in operations:
        if operation.startswith(f"{wire1} {operator} {wire2}") or operation.startswith(
            f"{wire2} {operator} {wire1}"
        ):
            print(operation)
            print(operation.split("->")[1].strip())
            return operation.split("->")[1].strip()


carry0 = None
carry1 = None
for i in range(45):
    n = "0" + str(i) if i < 10 else str(i)
    m1 = search(f"x{n}", f"y{n}", "XOR")
    n1 = search(f"x{n}", f"y{n}", "AND")
    carry1 = None
    z1 = r1 = None

    if carry0:
        r1 = search(carry0, m1, "AND")
        if not r1:
            n1, m1 = m1, n1
            swapped.add(m1)
            swapped.add(n1)
            r1 = search(carry0, m1, "AND")

        z1 = search(carry0, m1, "XOR")

        if m1 is None or m1.startswith("z"):
            m1, z1 = z1, m1
            swapped.add(m1)
            swapped.add(z1)

        if n1 is None or n1.startswith("z"):
            n1, z1 = z1, n1
            swapped.add(n1)
            swapped.add(z1)

        if r1 is None or r1.startswith("z"):
            r1, z1 = z1, r1
            swapped.add(r1)
            swapped.add(z1)

        carry1 = search(r1, n1, "OR")

    if carry1 is None or (carry1.startswith("z") and carry1 != "z45"):
        carry1, z1 = z1, carry1
        swapped.add(carry1)
        swapped.add(z1)

    carry0 = carry1 if carry0 else n1

print(",".join([item for item in swapped if item is not None]))

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

all_done = False
while not all_done:
    all_done = True
    lacking_wires = []
    for operation in operations:
        tmp = operation.split(" ")
        if wires[tmp[0]] == "-1" or wires[tmp[2]] == "-1":
            all_done = False
            if wires[tmp[0]] == "-1":
                lacking_wires.append(tmp[0])
            if wires[tmp[2]] == "-1":
                lacking_wires.append(tmp[2])

            continue
        if tmp[1] == "XOR":
            wires[tmp[4]] = str(int(wires[tmp[0]]) ^ int(wires[tmp[2]]))
        if tmp[1] == "OR":
            wires[tmp[4]] = str(int(wires[tmp[0]]) | int(wires[tmp[2]]))
        if tmp[1] == "AND":
            wires[tmp[4]] = str(int(wires[tmp[0]]) & int(wires[tmp[2]]))
    print(lacking_wires)
    print(sorted([(wire, wires[wire]) for wire in wires.keys()], key=lambda x: x[0]))
z_values = sorted([key for key in wires.keys() if key[0] == "z"])
print(z_values)
res_string = "".join([wires[key] for key in z_values])
print(res_string)
print(res_string[::-1])
print(int(res_string, 2))
print(int(res_string[::-1], 2))

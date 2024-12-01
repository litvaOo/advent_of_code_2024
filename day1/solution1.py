lines = []
with open("input.txt") as f:
    lines = f.readlines()
a, b = [], []
for line in lines:
    tmp = line.split()
    if len(tmp):
        a.append(int(tmp[0]))
        b.append(int(tmp[1]))
a.sort()
b.sort()
sum = 0
for i in range(len(a)):
    sum += abs(a[i] - b[i])
print(sum)

from collections import defaultdict

lines = []
with open("input.txt") as f:
    lines = f.readlines()
a, b = [], defaultdict(lambda: 0)
for line in lines:
    tmp = line.split()
    if len(tmp):
        a.append(int(tmp[0]))
        b[int(tmp[1])] += 1
sum = 0
for i in range(len(a)):
    sum += a[i] * b[a[i]]
print(sum)

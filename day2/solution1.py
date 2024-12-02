lines = []
with open("input.txt") as f:
    lines = f.readlines()

safe = 0
for line in lines:
    is_safe = 1
    levels = list(map(int, line.split()))
    if len(levels) == 0:
        continue
    if sorted(levels) == levels or sorted(levels) == levels[::-1]:
        for i in range(1, len(levels)):
            if abs(levels[i] - levels[i - 1]) > 3 or abs(levels[i] - levels[i - 1]) < 1:
                is_safe = 0
        safe += is_safe

print(safe)

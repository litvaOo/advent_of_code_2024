def check_levels(levels):
    is_safe = 1
    if sorted(levels) == levels or sorted(levels) == levels[::-1]:
        for i in range(1, len(levels)):
            if abs(levels[i] - levels[i - 1]) > 3 or abs(levels[i] - levels[i - 1]) < 1:
                is_safe = 0
    else:
        is_safe = 0
    return is_safe


lines = []
with open("input.txt") as f:
    lines = f.readlines()

safe = 0
unsafe = 0
for line in lines:
    levels = list(map(int, line.split()))
    if len(levels) == 0:
        continue
    if len(levels) - len(set(levels)) > 1:
        continue
    safe += check_levels(levels) or any(
        check_levels(levels[:i] + levels[i + 1 :]) for i in range(len(levels))
    )
print(safe)

secrets = []
with open("input.txt") as f:
    secrets = list(map(int, f.read().split()))

res = 0
subs = {}
for secret in secrets:
    patterns = []
    previous_price = secret % 10
    for i in range(2000):
        secret = (secret ^ (secret * 64)) % 16777216
        secret = (secret ^ (secret // 32)) % 16777216
        secret = (secret ^ (secret * 2048)) % 16777216
        tmp = secret % 10
        patterns.append((tmp - previous_price, tmp))
        previous_price = tmp
    seen = set()
    for i in range(len(patterns) - 4):
        pattern = tuple(x[0] for x in patterns[i : i + 4])
        value = patterns[i + 3][1]
        if pattern not in seen:
            seen.add(pattern)
            if pattern not in subs:
                subs[pattern] = value
            else:
                subs[pattern] += value
    res = max(subs.values())
print(res)

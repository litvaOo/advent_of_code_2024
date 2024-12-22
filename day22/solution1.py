secrets = []
with open("input.txt") as f:
    secrets = list(map(int, f.read().split()))

sum = 0
for secret in secrets:
    tmp = secret
    for i in range(2000):
        tmp = (tmp ^ (tmp * 64)) % 16777216
        tmp = (tmp ^ (tmp // 32)) % 16777216
        tmp = (tmp ^ (tmp * 2048)) % 16777216
    sum += tmp
    # print(secret, tmp)
print(sum)

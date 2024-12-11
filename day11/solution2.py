from functools import cache


lines = []
with open("input.txt") as f:
    lines = f.readlines()

line = lines[0].split()


@cache
def stone_sum(num, counter):
    if counter == 0:
        return 1
    if num == "0":
        return stone_sum("1", counter - 1)
    if len(num) % 2 == 1:
        return stone_sum(str(int(num) * 2024), counter - 1)
    return stone_sum(num[: len(num) // 2], counter - 1) + stone_sum(
        str(int(num[len(num) // 2 :])), counter - 1
    )


print(sum(stone_sum(num, 75) for num in line))

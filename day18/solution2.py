from collections import deque

memory_map = [["."] * 71 for _ in range(71)]
bytes_arr = []
with open("input.txt") as f:
    for line in f.readlines():
        tmp = list(map(int, line.split(",")))
        bytes_arr.append((tmp[1], tmp[0]))

for i in range(1024):
    memory_map[bytes_arr[i][0]][bytes_arr[i][1]] = "#"
visited = set()


def dfs(start_position):
    queue = deque([(start_position, 0)])
    global visited
    visited = {start_position}

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    target = (70, 70)

    while queue:
        pos, length = queue.popleft()
        if pos == target:
            return length
        x, y = pos
        for dx, dy in moves:
            new_x = x + dx
            new_y = y + dy
            new_pos = (new_x, new_y)
            if (
                0 <= new_x <= 70
                and 0 <= new_y <= 70
                and memory_map[new_y][new_x] != "#"
                and new_pos not in visited
            ):
                visited.add(new_pos)
                queue.append((new_pos, length + 1))

    return float("inf")


print(dfs((0, 0)))
print(len(bytes_arr))

for i in range(1023, len(bytes_arr)):
    print(i)
    visited = set()
    memory_map[bytes_arr[i][0]][bytes_arr[i][1]] = "#"
    if dfs((0, 0)) == float("inf"):
        print(i)
        print(bytes_arr[i])
        break


# for i in range(len(memory_map)):
#     for j in range(len(memory_map[i])):
#         if (i, j) in visited:
#             print("*", end="")
#         else:
#             print(memory_map[i][j], end="")
#     print()

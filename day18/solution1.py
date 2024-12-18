from collections import deque


memory_map = [["."] * 71 for _ in range(71)]
with open("input.txt") as f:
    i = 1
    for line in f.readlines():
        tmp = list(map(int, line.split(",")))
        memory_map[tmp[1]][tmp[0]] = "#"
        if i == 1024:
            break
        i += 1
visited = set()


def dfs(start_position):
    queue = deque([(start_position, 0)])
    global visited
    visited = {start_position}

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    target = (70, 70)

    while queue:
        pos, length = queue.popleft()
        print(pos)

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

for i in range(len(memory_map)):
    for j in range(len(memory_map[i])):
        if (i, j) in visited:
            print("*", end="")
        else:
            print(memory_map[i][j], end="")
    print()

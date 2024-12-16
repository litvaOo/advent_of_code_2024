from collections import deque

map = []
start = []
finish = []

# with open("input_test.txt") as f:
with open("input.txt") as f:
    for i, line in enumerate(f.readlines()):
        map.append(list(line)[:-1])
        for j, char in enumerate(line):
            if char == "S":
                start = i, j
                map[i][j] = "."
            if char == "E":
                finish = i, j
                map[i][j] = "."

visited = set()


def bfs(start_pos, start_direction):
    queue = deque([(start_pos, start_direction, 0, [start_pos])])

    best_costs = {}
    best_costs[(start_pos, start_direction)] = 0

    min_cost = float("inf")
    best_paths = []

    moves = {"LEFT": (0, -1), "RIGHT": (0, 1), "UP": (-1, 0), "DOWN": (1, 0)}

    while queue:
        pos, direction, cost, current_path = queue.popleft()

        if cost > min_cost:
            continue

        if pos == finish:
            if cost < min_cost:
                min_cost = cost
                best_paths = [current_path]
                global visited
                visited = set(current_path)
            elif cost == min_cost:
                best_paths.append(current_path)
                visited.update(current_path)
            continue

        for new_direction, (dx, dy) in moves.items():
            new_x, new_y = pos[0] + dx, pos[1] + dy
            new_pos = (new_x, new_y)

            if not (0 < new_x < len(map) and 0 < new_y < len(map[0])):
                continue
            if map[new_x][new_y] == "#":
                continue
            if new_pos in current_path:
                continue
            direction_cost = 1000 if direction != new_direction else 0
            new_cost = cost + 1 + direction_cost
            state_key = (new_pos, new_direction)
            if state_key in best_costs and best_costs[state_key] < new_cost:
                continue
            if new_cost > min_cost:
                continue
            best_costs[state_key] = new_cost
            new_path = current_path + [new_pos]
            queue.append((new_pos, new_direction, new_cost, new_path))

    return min_cost, best_paths


min_cost, best_paths = bfs(start, "RIGHT")
seats = set()
for path in best_paths:
    for seat in path:
        seats.add(seat)
for i in range(len(map)):
    for j in range(len(map[i])):
        if (i, j) in visited:
            print("*", end="")
        elif (i, j) == start:
            print("S", end="")
        elif (i, j) == finish:
            print("E", end="")
        else:
            print(map[i][j], end="")
    print()
print(len(seats))
print(min_cost)

import heapq

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

race_map = []
walls = set()
path = None
with open("input.txt") as file:
    for row, line in enumerate(file):
        for col, char in enumerate(line):
            if char == "#":
                walls.add((row, col))
            if char == "S":
                start = (row, col)
            if char == "E":
                end = (row, col)


def manhattan_distance(duple_1, duple_2):
    return abs(duple_1[0] - duple_2[0]) + abs(duple_1[1] - duple_2[1])


def sum_duples(duple_1, duple_2):
    return (duple_1[0] + duple_2[0], duple_1[1] + duple_2[1])


def neighbours(duple):
    return [sum_duples(duple, direction) for direction in DIRECTIONS]


def valid_neighbours(position):
    return [neighbour for neighbour in neighbours(position) if neighbour not in walls]


def shortest_path():
    queue = [(0, start)]
    path = []
    visited = set()
    while True:
        steps, position = heapq.heappop(queue)
        neighbours_to_check = valid_neighbours(position)
        for neighbour in neighbours_to_check:
            if neighbour in visited:
                continue
            path.append(neighbour)
            visited.add(neighbour)
            if neighbour == end:
                return path
            heapq.heappush(queue, (steps + 1, neighbour))


def saved_over_100():
    global path
    if path is None:
        path = shortest_path()
    cheats_count, cheats_count_20 = 0, 0
    for index, position in enumerate(path):
        difference = 99
        for other_position in path[index + 100 :]:
            difference += 1
            distance = manhattan_distance(position, other_position)
            if distance > 20:
                continue
            steps_gained = difference - distance
            if steps_gained < 100:
                continue
            cheats_count_20 += 1
            if distance <= 2:
                cheats_count += 1
    return cheats_count, cheats_count_20


print(saved_over_100())

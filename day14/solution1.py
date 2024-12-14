robots = []
quadrants = [0, 0, 0, 0]
with open("input.txt") as f:
    for line in f.readlines():
        if line == "\n":
            continue
        tmp = line.split()
        robot = {
            "p": tuple(map(int, tmp[0].split("=")[1].split(","))),
            "v": tuple(map(int, tmp[1].split("=")[1].split(","))),
        }
        robot_pos = [
            (robot["p"][0] + robot["v"][0] * 100) % 101,
            (robot["p"][1] + robot["v"][1] * 100) % 103,
        ]
        robots.append(robot_pos)
        if robot_pos[1] < 51:
            if robot_pos[0] < 50:
                quadrants[0] += 1
            if robot_pos[0] > 50:
                quadrants[1] += 1
        if robot_pos[1] > 51:
            if robot_pos[0] < 50:
                quadrants[2] += 1
            if robot_pos[0] > 50:
                quadrants[3] += 1
for i in range(103):
    for j in range(101):
        if [j, i] in robots:
            print("X", end="")
        else:
            print(".", end="")
    print("")
print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])
print(robots)

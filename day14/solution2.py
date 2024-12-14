robots_pos = set()
robots = []
with open("input.txt") as f:
    for line in f.readlines():
        if line == "\n":
            continue
        tmp = line.split()
        robot = {
            "p": tuple(map(int, tmp[0].split("=")[1].split(","))),
            "v": tuple(map(int, tmp[1].split("=")[1].split(","))),
        }
        robots.append(robot)
seconds = 1
while True:
    for robot in robots:
        robot_pos = (
            (robot["p"][0] + robot["v"][0] * seconds) % 101,
            (robot["p"][1] + robot["v"][1] * seconds) % 103,
        )
        if robot_pos in robots_pos:
            break
        else:
            robots_pos.add(robot_pos)
    else:
        print(seconds)
        break
    robots_pos = set()
    seconds += 1

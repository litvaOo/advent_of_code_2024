from functools import cache


@cache
def go_to_target(a, a_count, b, b_count, current_position, tokens, prize):
    if a_count > 100:
        if b_count > 100:
            return 0
        return go_to_target(
            a,
            a_count,
            b,
            b_count + 1,
            (current_position[0] + b[0], current_position[1] + b[1]),
            tokens + 1,
            prize,
        )
    if b_count > 100:
        if a_count > 100:
            return 0
        return go_to_target(
            a,
            a_count + 1,
            b,
            b_count,
            (current_position[0] + a[0], current_position[1] + a[1]),
            tokens + 3,
            prize,
        )

    if current_position[0] > prize[0] or current_position[1] > current_position[1]:
        return 0
    if current_position[0] == prize[0] and current_position[1] == prize[1]:
        return tokens
    a_press = go_to_target(
        a,
        a_count + 1,
        b,
        b_count,
        (current_position[0] + a[0], current_position[1] + a[1]),
        tokens + 3,
        prize,
    )
    if a_press == 0:
        return go_to_target(
            a,
            a_count,
            b,
            b_count + 1,
            (current_position[0] + b[0], current_position[1] + b[1]),
            tokens + 1,
            prize,
        )
    b_press = go_to_target(
        a,
        a_count,
        b,
        b_count + 1,
        (current_position[0] + b[0], current_position[1] + b[1]),
        tokens + 1,
        prize,
    )
    if b_press == 0:
        return a_press
    return min(a_press, b_press)


with open("input.txt") as f:
    sum = 0
    x, y, x_b, y_b, target_x, target_y = 0, 0, 0, 0, 0, 0
    for line in f:
        if line == "\n":
            continue
        if line.startswith("Button A:"):
            x, y = line.split()[2:4]
            x = int(x[:-1].split("+")[1])
            y = int(y.split("+")[1])
        if line.startswith("Button B:"):
            x_b, y_b = line.split()[2:4]
            x_b = int(x_b[:-1].split("+")[1])
            y_b = int(y_b.split("+")[1])
        if line.startswith("Prize:"):
            target_x, target_y = line.split()[1:3]
            target_x = int(target_x[:-1].split("=")[1])
            target_y = int(target_y.split("=")[1])
            res = go_to_target(
                (x, y), 0, (x_b, y_b), 0, (0, 0), 0, (target_x, target_y)
            )
            sum += res
    x, y, x_b, y_b, target_x, target_y = 0, 0, 0, 0, 0, 0
print(sum)

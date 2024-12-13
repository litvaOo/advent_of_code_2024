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
            target_x = int(target_x[:-1].split("=")[1]) + 10000000000000
            target_y = int(target_y.split("=")[1]) + 10000000000000
            a = (target_x * y_b - target_y * x_b) / (x * y_b - y * x_b)
            if a.is_integer():
                b = (target_x - x * a) / x_b
                if b.is_integer():
                    sum += a * 3 + b
                    print(sum)
                    print(a, b)

print(sum)

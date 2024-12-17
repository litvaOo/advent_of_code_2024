program = [2, 4, 1, 5, 7, 5, 1, 6, 4, 3, 5, 5, 0, 3, 3, 0]


def compute(a):
    output = []
    b = 0
    c = 0
    i = 0
    combo_operands = {
        0: lambda: 0,
        1: lambda: 1,
        2: lambda: 2,
        3: lambda: 3,
        4: lambda: a,
        5: lambda: b,
        6: lambda: c,
    }
    while i < len(program):
        opcode = program[i]
        operand = program[i + 1]
        match opcode:
            case 0:
                a = a // (2 ** combo_operands[operand]())
            case 1:
                b = b ^ operand
            case 2:
                b = combo_operands[operand]() % 8
            case 3:
                if a != 0:
                    i = operand
                    continue
            case 4:
                b = b ^ c
            case 5:
                output.append(combo_operands[operand]() % 8)
            case 6:
                b = a // (2 * combo_operands[operand]())
            case 7:
                c = a // (2 ** combo_operands[operand]())
        i += 2
    return output


a = 0
for n in range(1, len(program) + 1):
    new_a = a << 3
    target = program[len(program) - n :]
    while True:
        if compute(new_a) == target:
            a = new_a
            break
        new_a += 1
print(a)

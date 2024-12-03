def handle_mul(string, pointer):
    start = pointer
    if (
        string[pointer + 1] == "u"
        and string[pointer + 2] == "l"
        and string[pointer + 3] == "("
    ):
        num1 = ""
        pointer += 4
        while string[pointer].isnumeric():
            num1 += string[pointer]
            pointer += 1
        if string[pointer] != ",":
            print(string[start : pointer + 1])
            return 0
        pointer += 1
        num2 = ""
        while string[pointer].isnumeric():
            num2 += string[pointer]
            pointer += 1
        print(string[start : pointer + 1])
        if string[pointer] != ")":
            return 0
        try:
            return int(num1) * int(num2)
        except:
            return 0
    else:
        return 0


def handle_do(string, pointer, current):
    start = pointer
    if string[pointer + 1] != "o":
        return current
    if string[pointer + 2] == "n":
        if (
            string[pointer + 3] == "'"
            and string[pointer + 4] == "t"
            and string[pointer + 5] == "("
            and string[pointer + 6] == ")"
        ):
            print(string[start : pointer + 1])
            return False
        return current
    if string[pointer + 2] == "(" and string[pointer + 3] == ")":
        print(string[start : pointer + 1])
        return True
    return current


lines = ""
with open("input.txt", "r") as file:
    lines = file.read().replace("\n", "")

pointer = 0
do = True
sum = 0

while pointer < len(lines):
    if lines[pointer] == "m" and do:
        sum += handle_mul(lines, pointer)
    if lines[pointer] == "d":
        do = handle_do(lines, pointer, do)
    pointer += 1
print(sum)

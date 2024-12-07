lines = []
with open("input.txt") as f:
    lines = f.readlines()

sum = 0
for line in lines:
    result = int(line.split(":")[0])
    numbers = list(map(int, line.split(":")[1].split()))

    print(result, numbers)

    def sum_search(first_number, index, sign=""):
        print(first_number, sign, numbers[index])
        if index == len(numbers) - 1:
            return (
                first_number * numbers[index] == result
                or first_number + numbers[index] == result
            )
        if first_number > result:
            return False
        return sum_search(first_number * numbers[index], index + 1, "*") or sum_search(
            first_number + numbers[index], index + 1, "+"
        )

    if sum_search(numbers[0], 1):
        sum += result

    # break
print(sum)

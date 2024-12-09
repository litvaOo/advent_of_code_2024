lines = []
with open("input.txt") as f:
    lines = f.readlines()
id_counter = 0
file = True
array = []
for char in lines[0]:
    if char == "\n":
        continue
    if file:
        array.append([id_counter] * int(char))
        id_counter += 1
        file = False
    else:
        if int(char) != 0:
            array.append(["."] * int(char))
        file = True

start = 0
end = len(array) - 1
while end > start:
    if array[end][0] == ".":
        end -= 1
        continue
    for i in range(start, end):
        if array[i][0] == "." and len(array[i]) >= len(array[end]):
            diff = len(array[i]) - len(array[end])
            array[i], array[end] = array[end], ["."] * len(array[end])
            if diff > 0:
                array.insert(i + 1, ["."] * diff)
                end += 1
            break
    end -= 1
sum = 0
sum_counter = 0
for file in array:
    for i in file:
        if i == ".":
            sum_counter += 1
            continue
        sum += sum_counter * i
        sum_counter += 1
print(sum)

lines = []
with open("input.txt") as f:
    lines = f.readlines()
file = True
id_counter = 0
array = []
for char in lines[0]:
    if char == "\n":
        continue
    if file:
        array.extend([str(id_counter)] * int(char))
        id_counter += 1
        file = False
    else:
        array.extend(["."] * int(char))
        file = True
end = len(array) - 1
for i in range(len(array)):
    if array[i] == ".":
        array[i], array[end] = array[end], array[i]
        end -= 1
    while array[end] == ".":
        end -= 1
    if end <= i:
        break
sum = 0
for i, char in enumerate(array[: end + 1]):
    sum += i * int(char)
print(sum)

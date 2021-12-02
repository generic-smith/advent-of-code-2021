print("2.1")

horizontal = 0
depth = 0

lines = list(map(lambda x: x.split(), open("day2.txt")))

for direction, distance in lines:
    if direction == "down":
        depth += int(distance)
    elif direction == "up":
        depth -= int(distance)
    else:
        horizontal += int(distance)

print(horizontal * depth)


print("\n2.2")

horizontal = 0
depth = 0
aim = 0

lines = list(map(lambda x: x.split(), open("day2.txt")))

for direction, value in lines:
    if direction == "down":
        aim += int(value)
    elif direction == "up":
        aim -= int(value)
    else:
        horizontal += int(value)
        depth += int(value) * aim

print(horizontal * depth)
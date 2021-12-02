print("1.1")
increased_counter = 0
lines = list(map(int, open('day1.txt')))
for c, n in zip(lines, lines[1:]):
    if c < n:
        increased_counter += 1

print(increased_counter)

print("\n1.2")
# 1.2
increased_counter = 0
for c, n in zip(lines, lines[3:]):
    if c < n:
        increased_counter += 1
print(increased_counter)

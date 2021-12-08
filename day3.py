import pandas as pd

print("3.1")
reports = list(zip(*list(map(str, open('day3.txt')))))
gamma = 0
epsilon = 0

for c in range(0, len(reports)):
    bit = list(map(int, reports[-c - 1]))
    if sum(bit) > len(bit) // 2:
        gamma += 2 ** c
    else:
        epsilon += 2 ** c

print(gamma * epsilon)

print("\n3.2")

generator = 0
scrubber = 0

raw = list(map(str, open('day3.txt')))


def split(string):
    return [char for char in string[:-1]]


lol = list(map(split, raw))

df = pd.DataFrame(lol)
generator_remaining = df
scrubber_remaining = df

for c in range(0, len(reports)):
    # generator
    g_bit = list(map(int, generator_remaining[int("{}".format(c))]))
    # print(len(generator_remaining))
    if len(generator_remaining) > 1:
        if sum(g_bit) >= len(g_bit) / 2:
            generator_remaining = generator_remaining.loc[generator_remaining[int("{}".format(c))] == '1']
        else:
            generator_remaining = generator_remaining.loc[generator_remaining[int("{}".format(c))] == '0']

    # scrubber
    s_bit = list(map(int, scrubber_remaining[int("{}".format(c))]))
    # print(len(scrubber_remaining))
    if len(scrubber_remaining) > 1:
        if sum(s_bit) >= len(s_bit) / 2:
            scrubber_remaining = scrubber_remaining.loc[scrubber_remaining[int("{}".format(c))] == '0']
        else:
            scrubber_remaining = scrubber_remaining.loc[scrubber_remaining[int("{}".format(c))] == '1']

gen_output = "".join(list(generator_remaining.iloc[0]))
scrub_output = "".join(list(scrubber_remaining.iloc[0]))

print(int(gen_output, 2) * int(scrub_output, 2))

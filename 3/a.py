def value(c):
    val = ord(c)
    if val < 97:
        return 26 + val - 64
    else:
        return val - 96


values = []
with open("input.txt") as f:
    curr = []
    for line in f.readlines():
        line = line[:-1]
        curr.append(line)

        if len(curr) == 3:
            singleton = list(set(curr[0]).intersection(
                set(curr[1]).intersection(set(curr[2]))))[0]

            values.append(value(singleton))
            curr = []

print(sum(values))

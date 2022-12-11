
insns = []
with open("10/input.txt") as f:
    for line in f.readlines():
        insns.append(0)
        if line.startswith("addx"):
            val = int(line.split(" ")[1])
            insns.append(val)

reg = 1
values = []
for insn in insns:
    values.append(reg)
    reg += insn


def get_strength(cycle):
    return cycle * values[cycle - 1]


# print(sum([get_strength(cycle) for cycle in [20, 60, 100, 140, 180, 220]]))

# b

for m in range(6):
    row = ""
    for n in range(40):
        cycle = m * 40 + n
        sprite_loc = values[cycle]
        if (n - sprite_loc) ** 2 <= 1:
            # within 1
            row += "#"
        else:
            row += "."
    print(row)

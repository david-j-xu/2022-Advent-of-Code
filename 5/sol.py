with open("input.txt") as f:
    lines = f.readlines()

    stacks = {}

    for i in range(8):
        line = lines[i]
        vals = [line[j] for j in [1, 5, 9, 13, 17, 21, 25, 29, 33]]
        for (pile, val) in enumerate(vals):
            pile = pile + 1

            if val != " ":
                if pile in stacks:
                    stacks[pile].append(val)
                else:
                    stacks[pile] = [val]
    for key in stacks:
        stacks[key].reverse()

    for line in lines[10:]:
        split = line.split(" ")

        num = int(split[1])
        fro = int(split[3])
        to = int(split[5])

        from_pile = stacks[fro]
        to_pile = stacks[to]

        to_move = stacks[fro][-num:]
        # to_move.reverse()
        stacks[fro] = from_pile[:-num]
        stacks[to].extend(to_move)

for i in range(1, 10):
    print(stacks[i][-1])

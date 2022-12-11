import math

up, down, left, right = ((0, -1), (0, 1), (-1, 0), (1, 0))

# head = (0, 0)
# tail = (0, 0)

bridge = [(0, 0) for _ in range(10)]

tail_pos = set([(0, 0)])

instructions = []
with open("9/input.txt") as f:
    for line in f.readlines():
        insn, times = line[:-1].split(" ")
        for _ in range(int(times)):
            if insn == 'R':
                instructions.append(right)
            elif insn == 'L':
                instructions.append(left)
            elif insn == 'U':
                instructions.append(up)
            elif insn == 'D':
                instructions.append(down)


def adj(head, tail):
    return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1


def sgn(val):
    return 0 if val == 0 else 1 if val > 0 else -1


for insn in instructions:
    bridge[0] = (bridge[0][0] + insn[0], bridge[0][1] + insn[1])

    for i in range(9):
        if not adj(bridge[i], bridge[i + 1]):
            xdiff = sgn(bridge[i][0] - bridge[i + 1][0])
            ydiff = sgn(bridge[i][1] - bridge[i + 1][1])

            bridge[i + 1] = (bridge[i + 1][0] + xdiff,
                             bridge[i + 1][1] + ydiff)

    tail_pos.add(bridge[9])

print(len(tail_pos))

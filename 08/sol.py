import math

map = []

with open("8/test.txt") as f:
    for line in f.readlines():
        if line[-1] == '\n':
            line = line[:-1]
        curr = []
        for tree in line:
            curr.append(int(tree))
        map.append(curr)

m = len(map)
n = len(map[0])

visible = [[0] * n for _ in range(m)]

for row in range(m):
    # left
    max = -math.inf
    for col, tree in enumerate(map[row]):
        if tree > max:
            max = tree
            visible[row][col] = 1
    # right
    max = -math.inf
    for col, tree in reversed(list(enumerate(map[row]))):
        if tree > max:
            max = tree
            visible[row][col] = 1


for col in range(n):
    # top
    max = -math.inf
    for row in range(m):
        tree = map[row][col]
        if tree > max:
            max = tree
            visible[row][col] = 1
    # bottom
    max = -math.inf
    for row in range(m - 1, -1, -1):
        tree = map[row][col]
        if tree > max:
            max = tree
            visible[row][col] = 1

print(sum([sum(row) for row in visible]))

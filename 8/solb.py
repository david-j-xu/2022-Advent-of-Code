import math

map = []

with open("8/input.txt") as f:
    for line in f.readlines():
        if line[-1] == '\n':
            line = line[:-1]
        curr = []
        for tree in line:
            curr.append(int(tree))
        map.append(curr)

m = len(map)
n = len(map[0])
max = -math.inf

for row in range(1, m - 1):
    for col in range(1, n - 1):
        tree = map[row][col]
        score = 1

        i = 1
        # up
        while row - i >= 1 and map[row - i][col] < tree:
            i += 1
        score *= i
        i = 1
        # down
        while row + i < m - 1 and map[row + i][col] < tree:
            i += 1
        score *= i
        i = 1
        # right
        while col + i < n - 1 and map[row][col + i] < tree:
            i += 1
        score *= i
        i = 1
        # left
        while col - i >= 1 and map[row][col - i] < tree:
            i += 1
        score *= i

        if score > max:
            max = score

print(max)

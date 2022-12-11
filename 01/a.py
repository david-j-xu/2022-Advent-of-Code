
max = 0
elves = []
curr = 0
with open("./input.txt") as f:
    for line in f.readlines():
        line = line[:-1]
        if len(line) > 0:
            curr += int(line)
        else:
            elves.append(curr)
            curr = 0

print(sum(sorted(elves)[-3:]))

total = 0
with open("input.txt") as f:
    for line in f.readlines():
        vals = line.split(" ")
        theirs = vals[0]
        mine = vals[1][:-1]

        if mine == "X":
            total += 0
            if theirs == "A":
                total += 3
            elif theirs == "B":
                total += 1
            elif theirs == "C":
                total += 2
        elif mine == "Y":
            total += 3
            if theirs == "A":
                total += 1
            elif theirs == "B":
                total += 2
            elif theirs == "C":
                total += 3
        elif mine == "Z":
            total += 6
            if theirs == "A":
                total += 2
            elif theirs == "B":
                total += 3
            elif theirs == "C":
                total += 1

print(total)

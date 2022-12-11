
with open("6/input.txt") as f:
    for line in f.readlines():
        idx = 0
        flag = False
        while not flag:
            i = line[idx: idx + 14]
            flag = (len(set(i)) == 14)
            idx += 1
        print(idx)

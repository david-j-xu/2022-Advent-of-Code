with open("input.txt") as f:
    count = 0
    for line in f.readlines():
        line = line[:-1]
        vals = line.split(",")
        a = vals[0].split("-")
        b = vals[1].split("-")

        alo = int(a[0])
        ahi = int(a[1])

        blo = int(b[0])
        bhi = int(b[1])

        # a
        if (alo <= blo and ahi >= bhi) or (blo <= alo and bhi >= ahi):
            count += 1

        # b
        # if not (ahi < blo or bhi < alo):
        #   count += 1

    print(count)

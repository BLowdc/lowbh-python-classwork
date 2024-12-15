f = '92 0 286041 8034 34394 795 8 2051489'
stones = [int(i) for i in f.split() if i.isdigit()]

for blink in range(75):
    lslen = len(stones)
    i = 0
    while i < lslen:
        if stones[i] == 0:
            stones[i] = 1

        elif len(str(stones[i])) % 2 == 0:
            t = str(stones[i])
            l = len(t)
            left = t[:l//2]
            right = t[l//2:]
            stones[i] = int(left)
            stones.insert(i+1, int(right))
            i += 1
            lslen += 1

        else:
            stones[i] *= 2024
        #endif

        i += 1
    #endwhile

    print(blink, len(stones))



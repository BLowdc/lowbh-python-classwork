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
            half1 = t[:l//2]
            half2 = t[l//2:]
            stones[i] = int(half1)
            stones.insert(i+1, int(half2))
            i += 1
            lslen += 1

        else:
            stones[i] *= 2024
        #endif

        i += 1
    #endwhile

    print(blink, len(stones))



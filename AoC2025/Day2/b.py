with open("AoC2025\\Day2\\day2.txt", "r") as f:
    for line in f:
        ids = line.split(",")

for i in range(len(ids)):
    ids[i] = ids[i].split("-")

ans = 0
primes = [2, 3, 5, 7, 11, 13, 17, 21]

# main

for id in ids:
    for j in range(int(id[0]), int(id[1]) + 1):
        s = str(j)

        # for numbers with prime length
        if len(s) in primes:
            num = s[0]
            valid = True
            for k in range(1, len(s)):
                if s[k] != num:
                    valid = False
                # end if
            # next k
            if valid:
                ans += j
            # end if
        # end if

        # for numbers with non-prime length
        else:
            factors = []

            # finds all factors of len(s)
            for m in range(2, len(s) // 2 + 1):
                if len(s) % m == 0:
                    factors.append(m)
                # end if
            # next m

            # splits into substrings of length n
            for n in factors:
                valid = True

                # compares each of the substrings with the next
                for r in range(1, len(s) // n):
                    if s[n * (r - 1) : n * r] != s[n * r : n * (r + 1)]:
                        valid = False
                        break
                    # end if
                # next r

                if valid:
                    ans += j
                    break
                # end if
            # next n
        # end if
    # next j
# next id

print(ans)

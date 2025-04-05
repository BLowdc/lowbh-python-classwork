a = [int(s) for s in input().split()]
rank = 1
for i in range(len(a)):
    if i == 0:
        print(rank,end= ' ')
        fastestRank = rank
        fastest = a[0]
    elif a[i] - fastest < 10:
        print(fastestRank,end= ' ')
    else:
        print(rank,end= ' ')
        fastestRank = rank
        fastest = a[i]
    rank += 1
    
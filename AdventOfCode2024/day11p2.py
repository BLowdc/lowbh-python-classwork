f = '92 0 286041 8034 34394 795 8 2051489'
stones = [int(i) for i in f.split() if i.isdigit()]

DP = {}

def solve(r,t):
    if (r,t) in DP:
        return DP[(r,t)]
    if t == 0:
        ret = 1
    elif r == 0:
        ret = solve(1,t-1)
    elif len(str(r)) % 2 == 0:
        temp = str(r)
        l = len(temp)
        left = int(temp[:l//2])
        right = int(temp[l//2:])
        ret = solve(left, t-1) + solve(right, t-1)
    else:
        ret = solve(r*2024, t-1)
    DP[(r,t)] = ret
    return ret
#end function

def solveAll(t):
    return sum(solve(r,t) for r in stones)
#end function

print(solveAll(25))
print(solveAll(75))


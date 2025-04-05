post, rail, pick = [int(s) for s in input().split()]

pickMax = pick // 8
railMax = rail // 2
postMax = post - 1

num = min(pickMax,railMax,postMax)

print(num*2)

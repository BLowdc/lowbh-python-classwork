def countPassengers(ls) -> int:
    total = 0
    for elem in ls:
        total += elem[0]
        total -= elem[1]
    #next pair
    return total
#end function

nums = input().split(",")
ppl = []
for pair in nums:
    pair = [int(i) for i in pair.split(" ")]
    ppl.append(pair)
#next pair

print(countPassengers(ppl))


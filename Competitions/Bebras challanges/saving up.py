def saving_up(nums):
    c = 0
    saved = 0
    for n in nums:
        saved += n - 20
        c += 1
        if saved > 1000:
            return c

l = [int(i) for i in input().split() if i.isdigit()]
print(saving_up(l))
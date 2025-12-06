nums = []
operations = []
with open("AoC2025\\Day6\\input.txt", "r") as f:
    for line in f:
        nums.append(line.strip().split())

cols = len(nums[0])
rows = len(nums)
ans = 0

for i in range(cols):
    op = nums[-1][i]
    if op == "+":
        result = 0
        for j in range(rows-1):
            result += int(nums[j][i])
    elif op == "*":
        result = 1
        for j in range(rows-1):
            result *= int(nums[j][i])
    
    ans += result

print(ans)



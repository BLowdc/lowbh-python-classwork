nums = []
operations = []
with open("AoC2025\\Day6\\input.txt", "r") as f:
    for line in f:
        nums.append(line.strip("\n"))

operations = nums[-1].split()
cols = len(nums[0])
rows = len(nums) - 1
numbers = []
col = []

for i in range(cols):
    n = ''
    for j in range(rows):
        n += nums[j][i]
    if not n.isspace():
        col.append(int(n))
    else:
        numbers.append(col)
        col = []
if col:
    numbers.append(col)

ans = 0

for k in range(len(numbers)):
    op = operations[k]

    if op == "+":
        result = 0
        for num in numbers[k]:
            result += num
    else:
        result = 1
        for num in numbers[k]:
            result *= num

    ans += result

print(ans)
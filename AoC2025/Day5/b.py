with open("AoC2025\\Day5\\test.txt", "r") as f:
    lines = [line.strip() for line in f]
        
emptyLine = lines.index('')

ranges = [list(line.split("-")) for line in lines[:emptyLine]]
ranges = [list(map(int, r)) for r in ranges]

fresh = 0

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2][0]
    left = [x for x in arr if x[0] < pivot]
    middle = [x for x in arr if x[0] == pivot]
    right = [x for x in arr if x[0] > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

ranges = quick_sort(ranges)
merged_ranges = []
merged_ranges.append(ranges[0])

for r in range(1,len(ranges)-1):
    if ranges[r][0] < merged_ranges[-1][1]:
        merged_ranges.append([ranges[r-1][0],ranges[r][1]])

print(merged_ranges)
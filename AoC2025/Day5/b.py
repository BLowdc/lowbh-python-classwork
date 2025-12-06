with open("AoC2025\\Day5\\input.txt", "r") as f:
    lines = [line.strip() for line in f]

emptyLine = lines.index("")

ranges = [list(line.split("-")) for line in lines[:emptyLine]]
ranges = [list(map(int, r)) for r in ranges]

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

for r in range(1, len(ranges)):
    if ranges[r][0] <= merged_ranges[-1][1]:
        if ranges[r][1] > merged_ranges[-1][1]:
            merged_ranges[-1][1] = ranges[r][1]
    else:
        merged_ranges.append(ranges[r])

fresh = 0

for n in merged_ranges:
    fresh += n[1] - n[0] + 1

print(fresh)

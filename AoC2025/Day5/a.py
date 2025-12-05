with open("AoC2025\\Day5\\input.txt", "r") as f:
    lines = [line.strip() for line in f]
        
emptyLine = lines.index('')

ranges = [tuple(line.split("-")) for line in lines[:emptyLine]]
ranges = [tuple(map(int, r)) for r in ranges]

IDs = lines[emptyLine+1:]
IDs = tuple(map(int, IDs))

fresh = 0
for id in IDs:
    for range in ranges:
        if range[0] <= id <= range[1]:
            fresh += 1
            break

print(fresh)
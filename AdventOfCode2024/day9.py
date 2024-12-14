files = ''
spaces = ''
disk = []
ans = 0
with open("c:\\AOC24\\disk.txt", 'r') as t:
    for line in t:
        f = line

for i in range(0,len(f)+1,2):
    files += f[i]

for j in range(1,len(f),2):
    spaces += f[j]

for k in range(len(files)):
    for l in range(int(files[k])):
        disk.append(k)
    if k < len(spaces):
        for m in range(int(spaces[k])):
            disk.append('.')

left = 0
right = len(disk) - 1

while left < right:
    if disk[left] == '.':
        while disk[right] == '.':
            right -= 1
        disk[left] = disk[right]
        disk[right] = '.'
    else:
        left += 1
#end while

for i in range(len(disk)):
    if disk[i] != '.':
        ans += (i * disk[i])

print(ans)
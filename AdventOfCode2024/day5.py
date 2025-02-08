r = open("c:\\AOC24\\rules.txt","r")
u = open("c:\\AOC24\\pages.txt","r")
rules = {}
temp_rules = []
updates = []
valid_updates =[]
ans = 0

def isValid(ls,dict) -> bool:
    for i in range(len(ls)):
        left = page[:i]
        for num in left:
            if num in dict[ls[i]]:
               return False
    return True


for line in r:
    line = line.replace('|',' ')
    pair = [int(i) for i in line.split() if i.isdigit()]
    temp_rules.append(pair)
    rules[pair[0]] = []
#next line

for n in temp_rules:
    rules[n[0]].append(n[1])

for line in u:
    line = line[:-1]
    line = line.replace(',',' ')
    updates.append([int(i) for i in line.split() if i.isdigit()])
#next line

for page in updates:
    if isValid(page,rules):
        valid_updates.append(page)
    #end if
#next page

for correct_ls in valid_updates:
    l = len(correct_ls)
    ans += correct_ls[l // 2]
#next corrext_ls

print(ans)
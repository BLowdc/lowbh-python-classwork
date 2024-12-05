r = open("c:\\AOC24\\rules.txt","r")
u = open("c:\\AOC24\\pages.txt","r")
rules = {}
temp_rules = []
updates = []
invalid_updates =[]
ans = 0

def isValid(ls,dict) -> bool:
    for i in range(len(ls)):
        left = ls[:i]
        for num in left:
            if num in dict[ls[i]]:
               return False
    return True
#end function

def sort(ls,dict) -> list:
    for i in range(len(ls)):
        left = ls[:i]
        for j in range(len(left)):
            if left[j] in dict[ls[i]]:
                t = ls[i]
                ls[i] = ls[j]
                ls[j] = t
    return ls

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

updates[-1][-1] = 35

for page in updates:
    if not isValid(page,rules):
        invalid_updates.append(page)
    #end if
#next page


for ls in invalid_updates:
    ls = sort(ls,rules)
#next ls

print(invalid_updates)

for corrected_ls in invalid_updates:
    l = len(corrected_ls)
    ans += corrected_ls[l // 2]
#next correxted_ls

print(ans)

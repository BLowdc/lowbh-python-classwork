list_length = int(input("Enter the length of the list: "))
ls = []
count = 1
candidate = ""

for i in range(list_length):
    ls.append(input())

candidate = ls[0]
    
for j in range(1,list_length):
    if ls[j] == candidate:
        count += 1
    elif count > 0:
        count -= 1
    else:
        candidate = ls[j]
        count = 1

count = 0
        
for c in ls:
    if c == candidate:
        count += 1

if count > list_length // 2:
    print(candidate, "has the majority.")
else:
    print("There is no majority.")

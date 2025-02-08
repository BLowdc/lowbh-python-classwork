import quickSort

txt = input()
table = {}
order = []
for char in txt:
    if char not in table:
        if char == ' ':
            table["SPACE"] = 1
            order.append("SPACE")
            continue
        #end if
        table[char] = 1
        order.append(char)
    else:
        if char == ' ':
            table["SPACE"] += 1
            continue
        #end if
        table[char] += 1
    #endif
#next char

# print(quickSort.quickSort(order,0,len(order)-1))

for key in table:
    print(f"{key}: {table[key]} times")
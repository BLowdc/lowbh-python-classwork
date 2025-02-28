def findMaxPath(n) -> list:
    tree = [0 if val == 'None' else int(val) for val in nodes]
    max = 0
    for root in range(14,6,-1):
        path = []
        total = tree[0]
        i = root + 1
        while i != 1:
            total += tree[i-1]
            path.append(tree[i-1])
            i = i//2
        #end while
        path.append(tree[0])
        if total > max:
            max = total
            maxPath = path
        #end if
    #next root
    return maxPath
#end function

nodes = input().split()

ans = findMaxPath(nodes)
for j in range(len(ans)-1,-1,-1):
    print(ans[j],end=" ")
#next j
print("")
print(sum(ans))


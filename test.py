l1 = [1,2,3]
l2 = [9,8,7]
n1 = ''
n2 = ''
for i in range(len(l1)-1,-1, -1):
    n1 += str(l1[i])
for j in range(len(l2)-1,-1, -1):
    n2 += str(l2[j])

t = int(n1) +int(n2)
l3 = []
for k in range(len(str(t))-1,-1,-1):
    l3.append(str(t)[k])
print(l3)


            
def max_elem(ls):
    a = []
    for row in ls:
        a.append(max(row))
    return a

n = int(input("rows: ")) 
a = [[int(j) for j in input("elems: ").split()] for i in range(n)]
print(max_elem(a))
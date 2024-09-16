def sum_of_rows(ls):
    a = [0] * len(ls)
    for i in range(len(ls)):
        for elem in ls[i]:
            a[i] += elem
    return a

n = int(input("rows: ")) 
a = [[int(j) for j in input("elems: ").split()] for i in range(n)]
print(sum_of_rows(a))
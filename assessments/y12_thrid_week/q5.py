def multiply_diagonal(ls):
    a = 0
    b = 0
    for i in range(len(ls)):
        a += ls[i][i]
        b += ls[i][len(ls)-i-1]
    #next i
    return abs(a-b)
#endprocedure

n = int(input("rows: ")) 
a = [[int(j) for j in input("elems: ").split()] for i in range(n)]
print(multiply_diagonal(a))


def proc1(x:int, y: list)->None:
    x = x - 2
    y[0] = 0
#endprocedure
m = 8
n = [10]
proc1(m,n)
print(m,n)
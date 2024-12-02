n,i = (int(s) for s in input().split())
l = 0
c = 0
while l < i+1:
    l += len(str(n+c))
#end while
print(l)
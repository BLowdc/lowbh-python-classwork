
input = input()
a,b = input.split()

def findCounts(string):
    c = 1
    i = 0
    while i < len(string) - 1:
        print('letter', a[i])
        while a[i] == a[i+1]:
            c += 1
            i += 1
        #endwhile
        print(c, 'times')
        i += 1
    
    return

findCounts(a)
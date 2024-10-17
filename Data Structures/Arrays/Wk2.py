def search(name, max):
    n = input() 
    found = False 
    for i in range(max): 
        if name[i] == n: 
            return (i + 1) 
            found = True 
        #end if 
        if i == (max - 1) and not found: 
            return "Term not found"
        #end if 
    #next i 
#end function

name = ['john', 'max', 'peter']
print(search(name, len(name)))
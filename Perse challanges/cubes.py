def findVol(x1,y1,z1,l1,x2,y2,z2,l2) -> int:
    x = intersect(x1,x2,l1,l2)
    y = intersect(y1,y2,l1,l2)
    z = intersect(z1,z2,l1,l2)
    vol = x*y*z
    return vol
    
#end function

def intersect(a,b,la,lb):
    if a < b:
        sect = a+la-b
        if sect > 0:
            if sect <= lb:
                return sect
            else:
                return lb
        else:
            return 0
    elif b < a:
        sect = b+lb-a
        if sect > 0:
            if sect <= la:
                return sect
            else:
                return la
        else:
            return 0
    else:
        if la < lb:
            return la
        else:
            return lb
#end function

minx1 = int(input())
miny1 = int(input())
minz1 = int(input())
len1 = int(input())
minx2 = int(input())
miny2 = int(input())
minz2 = int(input())
len2 = int(input())

print(findVol(minx1,miny1,minz1,len1,minx2,miny2,minz2,len2))
def checkIPvalidity(a):
    for num in a:
        if num < 0 or num > 255:
            return False
        #end of
    #next num
    return True
#end function

s = input()
ip = [int(i) for i in s.split(".")]
print(*ip,sep=".")

if checkIPvalidity(ip):
    print("Valid IP address")
else:
    print("Invalid IP address")
#end if


def multiples(table,startnum,endnum,pupilName)->None:
    print("Hi",pupilName,"... here is your times table")
    for i in range(startnum, endnum+1):
        print(table,"x",i,"=",table * i)
    #next i
#end procedure

print("What is your name")
name = input()
print("Enter times table, start number and end number")
table = int(input())
startnum = int(input())
endnum = int(input())
multiples(table,startnum,endnum,name)
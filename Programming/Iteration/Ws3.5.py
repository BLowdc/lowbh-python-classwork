t1 = 0
t2 = 0
t3 = 0
for i in range(30):
    print("Student",i+1,"scores.")
    t1 += int(input("Test 1: "))
    t2 += int(input("Test 2: "))
    t3 += int(input("Test 3: "))
print("Average for test 1:",round(t1/30,1))
print("Average for test 2:",round(t2/30,1))
print("Average for test 3:",round(t3/30,1))
print("Overall average:", round((t1+t2+t3)/90,1))
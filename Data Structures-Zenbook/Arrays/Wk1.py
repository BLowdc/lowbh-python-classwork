nums = [] 
t = 0 
for _ in range(5): 
    nums.append(int(input())) 
#next _ 
for i in reversed(nums): 
    t += i 
    print(i) 
#next i 
print(t) 
print(t/5) 
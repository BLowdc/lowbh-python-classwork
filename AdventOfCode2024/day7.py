f = open("c:\\AOC24\\operators.txt","r")

t = 0
invalid = []

def findSol(target, nums):
    if len(nums) == 1:
        return nums[0] == target
    if findSol(target, [nums[0]+nums[1]] + nums[2:]):
        return True
    if findSol(target, [nums[0]*nums[1]] + nums[2:]):
        return True
    if findSol(target, [int(str(nums[0])+str(nums[1]))] + nums[2:]):
        return True
    return False
    
#end function

for line in f:
    target,nums = line.strip().split(':')
    nums = [int(i) for i in nums.split() if i.isdigit()]
    target = int(target)
    if findSol(target,nums):
        t += target
    #endif
#next line

print(t)
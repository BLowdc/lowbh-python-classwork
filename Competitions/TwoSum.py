def twoSum(nums,target):
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [seen[diff], i]
        else:
            seen[nums[i]] = i
print(twoSum([1,7,6,8,5,4,9,3,2],5))
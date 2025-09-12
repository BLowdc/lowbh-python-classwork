from math import ceil
mergedList = []
nums1 = [1,4]
nums2 = [2]
for i in range(len(nums1)):
    mergedList.append(nums1[i])
for j in range(len(nums2)):
    mergedList.append(nums2[j])
mergedList.sort()
m = ceil(len(mergedList) / 2)
if len(mergedList) % 2 == 0:
    print((mergedList[m] + mergedList[m+1]) / 2)
else:
    print(mergedList[m-1])
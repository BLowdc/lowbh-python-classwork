from collections import Counter
l1 = []
l2 = []
diff = 0
sim = 0
f = open("c:\list.txt","r")
for line in f:
    n1, n2 = (int(s) for s in line.strip().split())
    l1.append(n1)
    l2.append(n2)
#next line

def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1
# function to perform quicksort


def quickSort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)

def binarySearch(t,arr) -> int:
    up = len(arr) - 1
    low = 0
    while up >= low:
        mid = (up + low) // 2
        if arr[mid] > t:
            up = mid - 1
        elif arr[mid] < t:
            low = mid + 1
        else:
            return t
        #end if
    #end while
    return 0
#end function

quickSort(l1, 0, len(l1)-1)
quickSort(l2, 0, len(l2)-1)

for i in range(len(l1)):
    diff += abs(l1[i] -l2[i])
#next i

cList = Counter(l2)


for num in l1:
    if cList.get(num):
        sim += num * cList.get(num)
#next num

print(sim)


import random
import time

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

size = int(input("Enter the size of the array: "))
random_array = [random.randint(0, 100) for _ in range(size)]
# print("Original array:", random_array)
start_time = time.time()
merge_sort(random_array)
end_time = time.time()
# print("Sorted array:", random_array)
print("Time taken to sort the array:", end_time - start_time, "seconds")


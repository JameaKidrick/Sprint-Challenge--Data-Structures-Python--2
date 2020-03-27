import time
from bst import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

def selection_sort( arr ):
    # loop through n-1 elements

    for i in range(0, len(arr) - 1):
    # 1. Start with current index = 0
        smallest_index = i
        # 2. For all indices EXCEPT the last index:
        #     a. Loop through elements on right-hand-side 
        #     of current index and find the smallest element
        for j in range(i, len(arr) - 1):
            # CHECK WHICH NUMBER IS SMALLER AND MAKE SURE SOON-TO-BE SMALLEST_INDEX IS SMALLER THAN THE CURRENT SMALLEST_INDEX
            if arr[j + 1] < arr[i] and arr[j + 1] < arr[smallest_index]:
                smallest_index = j + 1
        #     b. Swap the element at current index with the
        #     smallest element found in above loop
        if smallest_index != i:
            num = arr[i]
            arr[i] = arr[smallest_index]
            arr[smallest_index] = num
    return arr

# Replace the nested for loops below with your improvements
# names_1 = selection_sort(names_1)
for name_1 in range(len(names_1)-1):
    BinarySearchTree(names_1[name_1]).insert(names_1[name_1 +1])
# for name_2 in names_2:
#     if BinarySearchTree(names_1[len(names_1)-1]).contains(name_2):
#         duplicates.append(name_2)
print(len(names_1), names_1[len(names_1)-1])

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

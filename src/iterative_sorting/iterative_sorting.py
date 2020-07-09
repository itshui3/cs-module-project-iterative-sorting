# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for l in range(cur_index + 1, len(arr)):
            if arr[l] < arr[smallest_index]:
                smallest_index = l
        # TO-DO: swap
        # Your code here
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr



# 1. Loop through your array
#     - Compare each element to its neighbor
#     - If elements in wrong position (relative to each other, swap them)
# 2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    sort_count = 1
    while sort_count > 0:
        sort_count = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                # perform swap
                sort_count += 1
                arr[i], arr[i+1] = arr[i+1], arr[i]


    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
# my custom version [not exactly actual count sort]
def counting_sort(arr, maximum=None):
    # Your code here
    if len(arr):
        maximum = arr[0]
    else:
        return []

# find max_val
    for i in arr:
        if i > maximum:
            maximum = i
        if i < 0:
            return "Error, negative numbers not allowed in Count Sort"

    count = [0] * (maximum + 1)

# iterate counters
    for i in arr:
        count[i] += 1

# build new_arr from counter basis
    new_arr = []
    for value, count in enumerate(count):
        for i in range(count):
            new_arr.append(value)

    return new_arr

# we build an aux array
# wherein the indexex are the values we want sorted
# and the values are the amount of duplicates

# ie. [0, 0, 0, 2, 0, 1]
# I have 0 - 0's, 0 - 1's, 0 - 2's, 2 - 3's, 0 - 4's, 1 - 5's

# in an auxiliary array, indexes are already sorted. Therefore I can append the amount of times
# indicated

def abs_counting_sort(arr):
    if not len(arr): return []
    if len(arr) == 1: return arr

    minimum = arr[0]
    maximum = arr[0]
    for i in arr:
        if i < minimum: minimum = -1 * i
        if i > maximum: maximum = i
    
    pos_arr = [0] * (maximum + 1)
    neg_arr = [0] * (minimum + 1)

    for i in arr:
        if i >= 0: pos_arr[i] += 1
        if i < 0: neg_arr[-1 * i] += 1

    sorted_arr = []
    for i in range(len(neg_arr)-1, 0, -1):
        if neg_arr[i] > 0:
            sorted_arr += [-1 * i] * neg_arr[i]


    for i, e in enumerate(pos_arr):
        if e > 0:
            sorted_arr += [i] * e
    
    return sorted_arr

            
# will I have to worry about having 0 in both arrays?
# I can partially account for this
# by stopping the backwards for-loop prematurely
# at index 0, thereby preventing clearing of array by 1
# missing the 0


arr3 = [1, 5, -2, 4, 3, -7, -20]

sorted_3 = abs_counting_sort(arr3)
print(arr3)
print(sorted_3)

# neg array needs to be in descending order
# then depending on the looping direction and order
# append will populate sorted_arr by angling loops as needed
# on the positive and negative count arrays
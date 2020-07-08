def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found

def re_linear_search(arr, target, cur=0):
    if cur == len(arr): return -1

    if target == arr[cur]: return cur

    return re_linear_search(arr, target, cur+1)


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    l = 0
    r = len(arr)-1

    while r >= l:

        middex = ((r - l) // 2) + l

        if target == arr[middex]:
            return middex
        
        elif target > arr[middex]:
            l = middex + 1

        elif target < arr[middex]:
            r = middex - 1

    return -1  # not found

def re_binary_search(arr, target):
    pass
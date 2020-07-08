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

# we perform an in place search so as to preserve the array's entirety for returning the target's index
def re_binary_search(arr, target, l=0, r=0):
    if not len(arr): return -1
    
    middex = (r - l) // 2 + l
    if target == arr[middex]: return middex

    elif target > arr[middex]:
        l=middex + 1
        if l <= r:
            return re_binary_search(arr, target, l=l, r=r)
        else:
            return -1
    elif target < arr[middex]:
        r=middex - 1
        if l <= r:
            return re_binary_search(arr, target, l=l, r=r)
        else:
            return -1
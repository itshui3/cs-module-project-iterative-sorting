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


    return -1  # not found

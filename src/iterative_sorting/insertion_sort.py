

def insertion_sort(arr):
    # i marks the beginning of the unsorted sub-list
    for i in range(1, len(arr)):

        curdex = i
        while curdex > 0:

            if arr[curdex] >= arr[curdex - 1]:
                break
            else:
                # arr[curdex - 1], arr[curdex] = arr[curdex], arr[curdex - 1]
                right_val = arr[curdex]
                left_val = arr[curdex - 1]
                arr[curdex] = left_val
                arr[curdex - 1] = right_val

                curdex -= 1
    return arr

# unsorted = [0, 5, 2, 3, 1, 8, 9, 2, 1, 3]

# print(insertion_sort(unsorted))

# print(__name__)
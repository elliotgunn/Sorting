def quicksort2(l, low, high):
    if low >= high:
        return l
    
    pivot_index = low 

    # partition 
    for i in range(low, high):
        if l[i] < l[pivot_index]:
            l[i], l[pivot_index + 1] = l[pivot_index + 1], l[i]
            l[pivot_index], l[pivot_index + 1] = l[pivot_index + 1], l[pivot_index]
            pivot_index += 1
    quicksort2(l, low, pivot_index)
    quicksort2(l, pivot_index + 1, high)

    return l

def quicksort(l):
    return quicksort2(l, 0, len(l))

l = [2, 9, 5, 3, 0]
quicksort(l)
# print(l)

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    """
    Merge two sorted arrays into one sorted order.
    """
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements # this makes a list of zeros the length of both arrays
    new_arr = []
    # TO-DO
    i_A = 0
    i_B = 0

    while i_A < len(arrA) and i_B < len(arrB):
        if arrA[i_A] < arrB[i_B]:
            new_arr.append(arrA[i_A])
            i_A += 1
        else:
            new_arr.append(arrB[i_B])
            i_B += 1
    
    # case 1: if i_A is maxed out
    if i_B < len(arrB):
        # loop through the remaining vars in i_B
        for i in range(len(arrB[i_B:])):
            new_arr.append(arrB[i_B])
            i_B +=1 
    
    # case 2: if i_B is maxed out
    if i_A < len(arrA):
        # loop through the remaining vars in i_A
        for i in range(len(arrA[i_A:])):
            new_arr.append(arrA[i_A])
            i_A +=1 

    return new_arr

print(merge([2, 4, 6], [3, 5]))
print(merge([5, 7, 9], [2, 4, 6]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    """
    Takes an array, divides it in half, sorts the arrays, then merges them back.

    Recursion: when it sorts the divided arrays, it does so by pass them to itself.
    A one-item list is already sorted. 

    Example:
    Merging two one-item lists generates a sorted two-item list. 
    Merging two two-item lists generates a sorted four-item list. 
    """
    if len(arr) > 1:
    # while data contains more than one item, split in half
        split_index = len(arr) // 2 # find floor to split array into two

        # keep splitting 
        arrA = merge_sort(arr[:split_index])
        arrB = merge_sort(arr[split_index:])

        # apply helper merge function
        return merge(arrA, arrB)
    else:
        return arr

print(merge_sort([2, 4, 6, 5, 7, 9]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

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
print(l)

# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


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

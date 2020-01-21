def insertion_sort(items):
    # split list into sorted and unsorted
    
    # for each element in unsorted
    for i in range(1, len(items)):
        print(items)
        # insert that element into the correct place in sorted
        # store the element in a temp variable
        temp = items[i]
        # shift all larger sorted elements to the right
        j = i
        while j > 0 and temp < items[j-1]:
            items[j] = items[j-1]
            j -= 1
        # insert the element after the first smaller element 
        items[j] = temp
    return items

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i # 0
        smallest_index = cur_index  # 0
        # TO-DO: find next smallest element on the right
        for n in range(cur_index + 1, len(arr)):
            if arr[smallest_index] > arr[n]:
                smallest_index = n           
        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr

# beej's solution

def selection_sort(l):
    for u in range(len(l)):
        min_index = u

        # now loop through the rest of the list, aka the unsorted index
        for s in range(u + 1, len(l)):
            # find the smallest value in the unsorted list
            if l[s] < l[min_index]:
                min_index = s
        # smallest value found. now swap! 
        l[u], l[min_index] = l[min_index], l[u]
    return l




# TO-DO:  implement the Bubble Sort function below

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                # bubble swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
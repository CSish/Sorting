# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    a_head = 0
    b_head = 0

    for i in range(0, len(merged_arr)):
        if a_head >= len(arrA):
            merged_arr[i] = arrB[b_head]
            b_head += 1
        elif b_head >= len(arrB):
            merged_arr[i] = arrA[a_head]
            a_head += 1
        elif arrA[a_head] <= arrB[b_head]:
            merged_arr[i] = arrA[a_head]
            a_head += 1
        else:
            merged_arr[i] = arrB[b_head]
            b_head += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) < 2:
        return arr

    mid = int(len(arr)/2)
    arr1 = arr[ : mid]
    arr2 = arr[mid : ]

    merged = merge(merge_sort(arr1),  merge_sort(arr2))
    return merged


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

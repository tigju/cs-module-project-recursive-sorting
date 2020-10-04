# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    # declare empty array
    merged_arr = [];
    # until arrA and arrB have elements
    while len(arrA)>0 and len(arrB)>0:
        # if the first value from arrA greater then the first value of arrB
        if arrA[0] > arrB[0]:    
            # add this value to merged array and remove it from arrB     
            merged_arr.append(arrB[0])
            arrB.pop(0)
        # otherwise (if value less then the value from arrB)
        else:
            # add this value to merged array and remove it from arrA
            merged_arr.append(arrA[0])
            arrA.pop(0)
    # append array with remaining values from arrA
    while len(arrA)>0:
        merged_arr.append(arrA[0])
        arrA.pop(0)
    # append array with remaining values from arrB
    while len(arrB) > 0:
        merged_arr.append(arrB[0])
        arrB.pop(0)
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # return arr if it has 0 or 1 values
    if len(arr) <= 1:
        return arr
    
    # find the middle index of array
    middle = len(arr)//2
    # split array in half
    left = arr[:middle]
    right = arr[middle:]
    # recursion happens here 
    left = merge_sort(left)
    right = merge_sort(right)
    # when recursion meets base case merge arrays
    arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass


print(merge([2,3,4], [1,5,7]))

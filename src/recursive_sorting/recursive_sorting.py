#Understand
#Plan
#Execute
#Reflect

# what is recursion ? Recursion is a way of programming or coding a problem, in which a function calls itself one or more times in its body. ... If a function definition fulfils the condition of recursion, we call this function a recursive function. Termination condition: A recursive function has to terminate to be used in a program.

## Rules for recursion
# 1. Must Have A Base Case
# 2. Must change State toward the base case 
# 3. Must call itself Recursively 

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements equall the length of array a + b
    elements = len(arrA) + len(arrB)
    # the merged array will be the 1st index of the elements in the array 
    merged_arr = [0] * elements

    # Your code here
    # create a loop that will run over all the elements in the final merged array
    # for loop for the elements in merged array 
    for i in range(len(merged_arr)):
    # if length of array A and B is greater than 0 we iterate of both
        if len(arrA) > 0 and len(arrB) > 0:
        # array A is less than array B we push into merged array and iterate
            if arrA[0] < arrB[0]:
                merged_arr[i] = arrA[0]
                arrA.remove(arrA[0])
            else:
                # if the merged arr = arrB
                merged_arr[i] = arrB[0]
                # array B delete array b first index 
                arrB.remove(arrB[0])
        else:
                # if length of array A equal to 0 we push into merged array and iterate
                if len(arrA) == 0:
                    # merged arr = array b
                    merged_arr[i] = arrB[0]
                    # array b delete array B index 0
                    arrB.remove(arrB[0])
                else: 
                    # merged arr = array a 
                    merged_arr[i] = arrA[0]
                    # array a delete array a first index
                    arrA.remove(arrA[0])

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    # if length of array is greater than or equal to 1 
    if len(arr) <= 1:
        # return array 
        return arr
        middle = len(arr) // 2 # find the middle of the array 
        left = arr[:middle] # dividing the array elements 
        right = arr[middle:] # into 2 halves 
        
        # divide list array and assign each half 
        left = merge_sort(left) # sorting first half 
        right = merge_sort(right) # sorting second half 
        arr = merge(left, right)
    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr

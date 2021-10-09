#A left rotation operation on an array of size  shifts each of the array's elements  unit to the left. 
# Given an integer, , rotate the array that many steps left and return the result.

def rotateLeft(d, arr):
    # Write your code here
    if range(len(arr)==1):
        return arr
    else:
        for i in range(d):
            idxone = arr[0]
            for j in range(0,len(arr)-1):
                arr[j] = arr[j+1]
            arr[len(arr)-1] = idxone
        
    return arr
#26. Remove Duplicates from Sorted Array
#Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.
#Since it is impossible to change the length of the array in some languages, 
# you must instead have the result be placed in the first part of the array nums. 
# More formally, if there are k elements after removing the duplicates, 
# then the first k elements of nums should hold the final result. 
# It does not matter what you leave beyond the first k elements.
#Return k after placing the final result in the first k slots of nums.
#Do not allocate extra space for another array. 
# You must do this by modifying the input array in-place with O(1) extra memory.

def removeDuplicates(nums):  
    if(len(nums)<2): # Check for arrays of 0 or 1, if thats the case just return the length of those arrays
        k = len(nums)
        return k
    else: 
        i=0 
        while i < (len(nums)-1): #While loop that goes 0 to the len of the array -1 cause I index i+1

            if (nums[i] == nums[i+1]): #if the value at the current index in the list is equal to the next index 
                    nums.pop(i+1)  # remove the index ahead of it, thus removing the duplicate, as its iterating
            else:
                i+=1 # move the index up by one

    return len(nums) # in the end return the number of remaining & unique elements in the list

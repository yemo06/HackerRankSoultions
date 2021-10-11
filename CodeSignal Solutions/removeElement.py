#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The relative order of the elements may be changed.
#Since it is impossible to change the length of the array in some languages, \
# you must instead have the result be placed in the first part of the array nums. 
# More formally, if there are k elements after removing the duplicates, 
# then the first k elements of nums should hold the final result.
#  It does not matter what you leave beyond the first k elements.
#Return k after placing the final result in the first k slots of nums.
#Do not allocate extra space for another array. 
# You must do this by modifying the input array in-place with O(1) extra memory.

def removeElement(nums, val):
        if (len(nums)==0): # If the length of the List is zero just retrun the value of 0
            return 0
        else:
            i=0 #Index variable
            while i < (len(nums)): # Loop through the entire array using a while loop

                if (nums[i] == val): #If the current value at the index of the nums list is equivalent to the proposed value 
                        nums.pop@(i)  #remove from the list, 
                        #No idex out of bounds beacause the while loop is set to go while there a re values in the list
                else:
                    i+=1 #else contiue to traveese the list

        return len(nums) #return the number af values in the List that are not val.
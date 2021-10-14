#Given an array a that contains only numbers in the range from 1 to a.length, 
# find the first duplicate number for which the second occurrence has the minimal index. 
# In other words, if there are more than 1 duplicated numbers, 
# return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. 
# If there are no such elements, return -1.
def firstDuplicate(a):

    if(len(a)<2):  # If the length of the list is less than two then there is no duplicates
        return -1 #return the negative one to show no duplicate was found
    else:
        lowidx = set() # Set because it only accepts unique values and the search time is O(1) Time complexity.
        for i in range(len(a)): # Loop through the array 
            if ( a[i] in lowidx): #if the element has appeared in the set 
                return a[i] #return the element because its a duplicate
            else: #else
                lowidx.add(a[i]) #add that element to the set
            
    return -1 # If no duplicates found return -1
    
    
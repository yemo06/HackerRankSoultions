#Given an array of integers, find the pair of adjacent elements 
# that has the largest product and return that product.

'''
Parameters:
    inputArray (List): List with all the number to br mitipled
Returns:
    maxproduct the maximum adjacent multiplication 
'''
def adjacentElementsProduct(inputArray):
    if (len(inputArray) == 2): # If the inputArray only has two items that means that there product is already the max
        return inputArray[0] * inputArray [1] #return the product of the 2 numbers
    else:
        maxproduct = inputArray[0] * inputArray [1] #initialze the max as the product of the first 2 elements
        for i in range(1,(len(inputArray)-1),1): #for loop in range of: start: 1 to offest the first adjacent product, 
        #stop: input array -1 so the index doesnt go out of bounds, step is the loop is moving up by one
            currentproduct = inputArray[i] * inputArray[i+1] # The current product is the following adjacent values
            if ((max(maxproduct,currentproduct))==currentproduct): #Use the Max fuction to find the largest of the two numbers and check if max will change
                maxproduct = currentproduct #If the current product is larger, the current prodcut become the new maxproduct 
            
    return maxproduct
            
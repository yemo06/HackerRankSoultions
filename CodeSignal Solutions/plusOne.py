#You are given a large integer represented as an integer array digits, 
# where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.
#Increment the large integer by one and return the resulting array of digits.

def plusOne(self, digits: List[int]) -> List[int]:
    
    for i in range(len(digits)-1, 0, -1):
        if(digits[i] < 9):
            digits[i]+=1
            return digits
        else:
            digits[i]=0 
    print(digits)    
    digits.insert(0,1)
    return digits
    
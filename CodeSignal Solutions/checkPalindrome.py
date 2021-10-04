#Given the string, check if it is a palindrome.
'''
 Parameters:
    inputString (String): String being checked if it's a palindrome
    Returns:
    bool: True  if palindrome 
    or
    bool: False  If not palindrome
'''
def checkPalindrome(inputString):
    reverseString = "" # Intialize and empty string to hold the reversed String
    for i in range((len(inputString)-1),-1, -1): # for loop that loops throught the inputString backwards, from the end to start
        reverseString += inputString[i] # Add the contents of the inputString to the current value of the reverseString
        
    if(inputString == reverseString): #Checks if the inputString and the reverseString are equivalent 
        return True #if yes true
    else: #if no false
        return False


result = "abba"
result2 = "racecar"
result3 = "a"
result4 = "appapa"
    
print (result)  #True
print (result2) #True
print (result3) #True
print (result4) #False
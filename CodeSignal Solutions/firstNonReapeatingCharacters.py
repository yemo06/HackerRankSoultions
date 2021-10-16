#Given a string s consisting of small English letters, 
# find and return the first instance of a non-repeating character in it. 
# If there is no such character, return '_'.

def firstNotRepeatingCharacter(s):
    
    nonRepeat = dict.fromkeys(s,0) #Creating a dictiionary from the list to hold the individual letters as key and there frequecy as values
    for i in range(len(s)): #Loop through the length of the string
        if(s[i] in nonRepeat): # if a letter of the string s in the list of keys in the dictionary
            nonRepeat[s[i]] +=1 #increment the value matching string letter in the list to the one key in the dictionary
            
    
    for letter in nonRepeat: # Loop again though each letter
        if (nonRepeat[letter] == 1): # if the letter key in the dictionary equals one 
            return letter #Immediately return the letter as the first "Non repeating character"
    
    return '_' # If there is no "Non repeating character" return the "_"
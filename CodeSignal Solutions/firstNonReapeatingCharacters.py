#Given a string s consisting of small English letters, 
# find and return the first instance of a non-repeating character in it. 
# If there is no such character, return '_'.

def firstNotRepeatingCharacter(s):
    
    nonRepeat = dict.fromkeys(s,0)
    for i in range(len(s)):
        if(s[i] in nonRepeat):
            nonRepeat[s[i]] +=1
            
    
    for letter in nonRepeat:
        if (nonRepeat[letter] == 1):
            return letter
    
    return '_'
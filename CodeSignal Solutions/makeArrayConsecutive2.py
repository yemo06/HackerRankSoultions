#Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, 
# each statue having an non-negative integer size. Since he likes to make things perfect, 
# he wants to arrange them from smallest to largest 
# so that each statue will be bigger than the previous one exactly by 1. 
# He may need some additional statues to be able to accomplish that. 
# Help him figure out the minimum number of additional statues needed.

def makeArrayConsecutive2(statues):
    if (len(statues)==1): # If there is only one statue....,
        return 0 #you dont have any gaps to fill.
    else:
        statues.sort() # Sort the function to make it easier to find gaps in array 
        #OR
        # for i in range(len(statues)-1):
        #     if (statues[i]> statues[i+1]):
        #         holder = statues[i]
        #         statues[i] = statues[i+1]
        #         statues[i+1]= holder
        
        makeConsecutivecount = 0 #counter int to keep track of how many numbers are needed to make the list comsecutive
        for i in range(len(statues)-1): #For the length of the statues list -1 because we index the list with 1 ahead of the current index
            if(statues[i+1] != statues[i]+1): # Check if the indexes are consecutive 
                makeConsecutivecount += ((statues[i+1] - statues[i])-1) #If not then subtract the difference of the gap -1 to get the amount needed
            else:
                continue # continue with the loop
                
        return makeConsecutivecount

statues = [1,2,5, 9]
statues2 = [1]
statues3 = [-1,2,-5, 9,6,-10]
statues4 = [8,3,1,4,7]

print(makeArrayConsecutive2(statues)) #5
print(makeArrayConsecutive2(statues2)) #0
print(makeArrayConsecutive2(statues3)) #14
print(makeArrayConsecutive2(statues4)) #3
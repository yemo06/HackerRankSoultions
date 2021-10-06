#Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, 
# each statue having an non-negative integer size. Since he likes to make things perfect, 
# he wants to arrange them from smallest to largest 
# so that each statue will be bigger than the previous one exactly by 1. 
# He may need some additional statues to be able to accomplish that. 
# Help him figure out the minimum number of additional statues needed.

def makeArrayConsecutive2(statues):
    if (len(statues)==1):
        return 0
    else:
        statues.sort()
        #OR
        # for i in range(len(statues)-1):
        #     if (statues[i]> statues[i+1]):
        #         holder = statues[i]
        #         statues[i] = statues[i+1]
        #         statues[i+1]= holder
        
        makeConsecutivecount = 0 
        for i in range(len(statues)-1):
            if(statues[i+1] != statues[i]+1):
                makeConsecutivecount += ((statues[i+1] - statues[i])-1)
            else:
                continue
                
        return makeConsecutivecount
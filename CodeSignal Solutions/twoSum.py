#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

def twoSum(nums, target) :
        returnList = []
        if(len(nums)==2):
            returnList.append(0)
            returnList.append(1)
            return returnList
        else:
            for i in range(len(nums)-1):
                for j in range(i+1,len(nums),1):
                    if(nums[i]+nums[j] == target):
                        returnList.append(i)
                        returnList.append(j)
                        return returnList
                    else:
                        continue
        
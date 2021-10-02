#Given a year, return the century it is in. 
#The first century spans from the year 1 up to and including the year 100, 
#the second - from the year 101 up to and including the year 200, etc.

def centuryFromYear(year):
    century = 100 
    if (year % century == 0): #If the the year divided 100 remainder is 0  
        return (year// century) #Then return the division result as the the century the year belongs in
    else: # If not the case 
        return (year//century)+1 #The year belongs in the following century so add 1 to the result of the division

result = centuryFromYear(1906)
result2 = centuryFromYear(2000)
result3 = centuryFromYear (1)

print (result) # 20
print (result2) #20
print (result3) # 1



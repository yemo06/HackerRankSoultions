# Problem Statement :
# Let's learn about list comprehensions! You are given three integers X,Y and Z representing the dimensions of a cuboid along with an integer N. You have to print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to N. Here, 0<=i<=X; 0<=j<=Y; 0<=k<=Z


# Input Format :
# Four integers X,Y,Z and N each on four separate lines, respectively.

# Constraints :
# Print the list in lexicographic increasing order.


#Solution

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
#  "[i,j,k]"" denotes the tuple form I want the entries in this list comprehension to be
# The cool thing about list coomprehensions is that what would normally be a triple nested for loop becomes-
#-three individual statements whose range is "+1" of the actual variables so that they will include the number given as well in range
# finally th if statement is added that sums the tulpes generated and compares them to m to make sure they are not equivalnt (!=) to N
# "newlist" contains the the newly generatd list and promptly prints it out

    
    newlist = [[i,j,k] for i in range (x+1) for j in range (y+1) for k in range (z+1) if sum([i,j,k])!= n]
    print (newlist)

    # I enjoyed this solution particularly because I had never seen what a List comprehension was before-
    # - and had to figure it out through alot research and learning which I enjoy.
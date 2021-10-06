#Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.
def shapeArea(n):
    if (n==1):
        return 1
    else:
        Area = (n * n) + (n-1) * (n-1)
        return Area
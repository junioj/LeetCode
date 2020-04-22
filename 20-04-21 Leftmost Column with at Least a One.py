# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        y=binaryMatrix.dimensions()
	j=0
        i=y[1]-1
        col=-1
	while(i>=0 and j<y[0]):
            if(binaryMatrix.get(j,i)==1):
                col=i
                i=i-1
            else:
                j=j+1
                    
        return col

# I made a video: https://www.youtube.com/watch?v=N1Bx1UjD2lQ
#
# Problem: find the leftmost column which has at least one "1" in it
#
# Example:
# [0 0]
# [1 1]
# Column 0 is the leftmost column with at least one 1, so return 0
#
# Each column is in increasing order (if i[j] is 1, then i[j+1]...i[n] are all 1)
# Every element is 0 or 1
# Maximum of 100 rows and 100 columns
# Cannot access get() more than 1000 times
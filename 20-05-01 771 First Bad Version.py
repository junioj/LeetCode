# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left=1
        right=n
        while(right>left):
            mid=floor((right-left)/2)+left
            # print(right,left,mid)
            if(isBadVersion(mid)):
                right=mid
            else:
                left=mid+1
        return left
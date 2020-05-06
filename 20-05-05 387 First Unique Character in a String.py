import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = collections.OrderedDict()
        for x in s:
            if x in d:
                d[x]=d[x]+1
            else:
                d[x]=1
                
        f=""
        
        for x in d:
            if d[x]==1:
                f=x
                break
        
        if(f==""):
            return -1
        
        return s.index(f)
        
# Problem: 
# Given a string, find the first non-repeating character in it 
# and return it's index. If it doesn't exist, return -1.
# Note: You may assume the string contain only lowercase letters.

# Examples:
# s = "leetcode"
# return 0.
# s = "loveleetcode",
# return 2.
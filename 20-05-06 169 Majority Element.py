import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s=Counter(nums)
        for x in s:
            if s[x]>=(len(nums)/2):
                return x
                
# Problem: Given an array of size n, find the majority element. 
# The majority element is the element that appears more than floor(n/2) times.
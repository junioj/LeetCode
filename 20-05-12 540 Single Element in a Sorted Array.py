import collections
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        for x in count:
            if count[x]!=2:
                return x

# Problem: You are given a sorted array consisting of only integers where 
# every element appears exactly twice, except for one element which appears 
# exactly once. Find this single element that appears only once.
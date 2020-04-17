class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # This solution passed 17/18 test cases.
        x=0
        y=0
        z=1
        nums2=[]
        
        while(x<len(nums)):
            if(y!=x):
                z=z*nums[y]
                # print(nums[x],nums[y])
            if(y==len(nums)-1):
                nums2.append(z)
                x=x+1
                z=1
                y=0
            else:
                y=y+1
            
        return nums2
    
# Problem: Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
# Solve without division in O(n) time. 

# Example:
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# (2*3*4=24, etc.)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProd = [0]*(len(nums))
        rightProd = [0]*(len(nums))
        leftProd[0]=1
        rightProd[len(nums)-1]=1
        
        for x in range(1,len(leftProd)):
            leftProd[x]=leftProd[x-1]*nums[x-1]
            
        # print(leftProd)
        for x in range(len(rightProd)-2,-1,-1):
            rightProd[x]=rightProd[x+1]*nums[x+1]
            
        # print(rightProd)
        for x in range(0,len(nums)):
            nums[x]=leftProd[x]*rightProd[x]
            
        return nums
    
# Problem: Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
# Solve without division in O(n) time. 

# Example:
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# (2*3*4=24, etc.)
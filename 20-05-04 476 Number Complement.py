class Solution:
    def findComplement(self, num: int) -> int:
    
        # A much more concise solution could be obtained using bitwise
        # operators. The following solution implements algorithms
        # more directly.
        
        g=[]
        
        def binary (num1: int, nums: list) -> list:
            if(num1>1):
                binary(num1//2, nums)
            nums.append(num1%2)
            return nums
        
        helper=binary(num,g)
        
        # print(helper)
        
        h=[]
        
        for x in helper:
            if x==1:
                h.append(0)
            else:
                h.append(1)
                
        # print(h)
        
        ans=0
        
        for x in range(0,len(h)):
            ans+=h[x]*(2**(len(h)-x-1))
            
        return ans
        
# Question: Given a positive integer, output its complement number. The complement 
# strategy is to flip the bits of its binary representation.

# Example:
# Input: 5 Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its 
# complement is 010. So you need to output 2.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

	n=0        

        for x in range(0,len(nums)):
            if nums[x]==0:
                n=n+1

        for x in range(0,n):
            nums.remove(0)
            nums.append(0)
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int l=0, k=0;
        for(int i=0;i<nums.length;i++){
            for(int j=0;j<nums.length;j++){
                if((nums[i]+nums[j]==target)&&(i!=j)){
                    k=j;
                    l=i;
                }
            }
        }
        return new int[]{l,k};
    }
}
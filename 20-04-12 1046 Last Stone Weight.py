class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        # print(stones)
        x=0
        y=0
        while(len(stones)>1):
            if(stones[x]>stones[x+1]):
                y=stones[x]-stones[x+1]
                del stones[x]
                del stones[x]
                stones.insert(0,y)
                stones.sort(reverse=True)
                # print(stones)
            else:
                del stones[x]
                del stones[x]
                # print(stones)
        
        if(len(stones)>0):
            return stones[x]
        return 0
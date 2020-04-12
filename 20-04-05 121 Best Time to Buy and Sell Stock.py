class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max(prices)!=min(prices) or 
        k=0
        
        j=[]
        n=[]
        
        for a in range(0,len(prices)-1):
            if prices[a]<(prices[a+1]):
                j.append(a)
        
        if(len(j)>0):
            for a in range(0,len(j)):
                n.append(max(prices[j[a]:len(prices)])-prices[j[a]])
            return max(n)

	return 0
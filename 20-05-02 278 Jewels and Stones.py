class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = []
        count=0
        for x in J:
            jewels.append(x)
        for x in S:
            if x in jewels:
                count=count+1
        return count
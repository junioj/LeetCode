class Solution:
    def frequencySort(self, s: str) -> str:
        count = collections.Counter(s).most_common()
        newstring = ""
        for x in count:
            for y in range(0,x[1]):
                newstring += x[0]
        return newstring
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for x in ransomNote:
            if x in magazine:
                magazine=magazine[:magazine.find(x)] + magazine[magazine.find(x)+1:]
                ransomNote=ransomNote[:ransomNote.find(x)] + ransomNote[ransomNote.find(x)+1:]
        if len(ransomNote)==0:
            return True
        return False
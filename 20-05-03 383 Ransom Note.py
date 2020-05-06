class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for x in ransomNote:
            if x in magazine:
                magazine=magazine[:magazine.find(x)] + magazine[magazine.find(x)+1:]
                ransomNote=ransomNote[:ransomNote.find(x)] + ransomNote[ransomNote.find(x)+1:]
        if len(ransomNote)==0:
            return True
        return False
        
# Question: Given an arbitrary ransom note string and another string containing 
# letters from all the magazines, write a function that will return true if the
# ransom note can be constructed from the magazines ; otherwise, it will return false.
# Each letter in the magazine string can only be used once in your ransom note.

# Examples:
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
# canConstruct("abse", "seab") -> true
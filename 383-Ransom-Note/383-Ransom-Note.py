class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        for m in magazine:
            if m in ransomNote:
                idx = ransomNote.index(m)
                ransomNote.pop(idx)
        if len(ransomNote) == 0:
            return True
        else:
            return False
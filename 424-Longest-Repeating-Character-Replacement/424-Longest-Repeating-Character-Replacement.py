class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charDict = {char : 0 for char in list(set(s))}
        windowLen = 0
        l, r = 0,0
        while l < len(s) and r < len(s):
            charDict[s[r]] += 1 
            windowLen = len(s[l:r+1])
            if (windowLen - max(charDict.values())) > k:
                charDict[s[l]] -= 1
                l += 1
                r += 1
            else:
                r += 1

        return sum(charDict.values())
        

sol = Solution()
print(sol.characterReplacement("AABABBA", 1))
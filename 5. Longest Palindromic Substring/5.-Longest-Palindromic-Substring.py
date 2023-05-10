class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expandFromMid(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
    
        res = []
        for i in range(len(s)):
            if len(expandFromMid(i,i, s)) > len(expandFromMid(i, i+1, s)):
                if len(res) < len(expandFromMid(i,i, s)):
                    res = expandFromMid(i,i, s)
            else:
                if len(res) < len(expandFromMid(i, i+1, s)):
                    res = expandFromMid(i, i+1, s)
        return res
    
    
solution = Solution()
print(solution.longestPalindrome("cbbd"))
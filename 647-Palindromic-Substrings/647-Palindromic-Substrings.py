class Solution:
    def isPelin(self, s):
        return s == s[::-1]
    def countSubstrings(self, s: str) -> int:
        answer = 0
        for i in range(0, len(s)):
            for j in range(i+1,len(s)+1):
                if self.isPelin(s[i:j]):
                    answer += 1
        return answer
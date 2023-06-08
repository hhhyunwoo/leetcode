from math import inf

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        tDict = {char: 0 for char in list(set(t))}
        for i in range(m):
            tDict[t[i]] += 1

        ansL, ansR = 0, inf 
        l, r = 0, 0

        if s[0] in tDict.keys():
            tDict[s[0]] -= 1
        while l < n and r < n:
            flag = True
            for value in tDict.values():
                if value > 0:
                    flag = False
                    break

            if flag:
                if r-l < ansR - ansL:
                    ansR, ansL = r, l
                if l < n and s[l] in tDict.keys():
                    tDict[s[l]] += 1
                l += 1
            else:
                r += 1
                if r < n and s[r] in tDict.keys():
                    tDict[s[r]] -= 1

        if inf in [ansL, ansR]:
            return ""
        else:
            return s[ansL:ansR+1]

sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))
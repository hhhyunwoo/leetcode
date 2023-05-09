class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestLen = 0
        ansDict = {}
        for i in range(0, len(s)):
            ansDict[i] = []
            for j in range(i, len(s)):
                if s[j] in ansDict[i]:
                    break
                ansDict[i].append(s[j])
        print(ansDict)
        for k, v in ansDict.items():
            if longestLen < len(v):
                longestLen = len(v)
        return longestLen
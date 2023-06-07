class Solution:
    def frequencySort(self, s: str) -> str:
        sDict = {s[i]: 0 for i in range(len(s))}
        for i in range(len(s)):
            sDict[s[i]] += 1

        sSortedArr = [k for k,v in sorted(sDict.items(), key=lambda item: item[1], reverse=True)]

        answer = []
        for c in sSortedArr:
            for _ in range(sDict[c]):
                answer.append(c)
        return answer

sol = Solution()
print(sol.frequencySort("Aabb"))
from typing import List

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = [i for i in range(len(s))]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            x = find(x)
            y = find(y)

            if x < y:
                parent[y] = x
            else:
                parent[x] = y

        for x,y in pairs:
            union(x,y)

        rootDict = {i:[] for i in range(len(s))}
        for i in range(len(s)):
            rootDict[find(i)].append(s[i])

        for k in rootDict.keys():
            rootDict[k] = sorted(rootDict[k])

        answer = ""
        for i in range(len(s)):
            answer += rootDict[find(i)].pop(0)
        return answer 

print(Solution().smallestStringWithSwaps("dcab", [[0,3],[1,2],[0,2]]))
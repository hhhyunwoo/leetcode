from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answers = []
        anagramDict = {}
        for str in strs:
            sortedStr = ''.join(sorted(str))
            if sortedStr in anagramDict.keys():
                anagramDict[sortedStr].append(str)
            else:
                anagramDict[sortedStr] = [str]
        print(list(anagramDict.values()))
        return list(anagramDict.values())

solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
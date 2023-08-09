class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        patternDict = {}
        wordDict = {}

        if len(s) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in patternDict.keys():
                if patternDict[pattern[i]] != s[i]:
                    return False
            else:
                if s[i] in wordDict.keys():
                    return False
                patternDict[pattern[i]] = s[i]
                wordDict[s[i]] = 1
        return True
            
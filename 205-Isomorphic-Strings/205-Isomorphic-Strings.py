class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s, t = list(s), list(t)
        sDict, tDict = {}, {}
        idx = 0
        for i in range(len(s)):
            if s[i] in sDict.keys():
                s[i] = sDict[s[i]]
            else:
                sDict[s[i]] = idx
                s[i] = idx
                idx += 1

        idx = 0
        for i in range(len(t)):
            if t[i] in tDict.keys():
                t[i] = tDict[t[i]]
            else:
                tDict[t[i]] = idx
                t[i] = idx
                idx += 1
                
        if s == t: return True
        else: return False
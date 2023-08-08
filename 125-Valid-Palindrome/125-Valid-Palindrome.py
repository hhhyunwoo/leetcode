import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = True
        updatedStr = re.compile('[^a-z0-9]').sub('', s.lower())
        print(updatedStr)
        i, j= 0, len(updatedStr)-1
        while i<=j:
            if updatedStr[i] == updatedStr[j]:
                i += 1
                j -= 1
            else:
                ans = False
                break
        return ans
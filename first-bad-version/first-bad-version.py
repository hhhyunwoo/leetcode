# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

from math import inf

class Solution:
    def firstBadVersion(self, n: int) -> int:
        answer = inf
        l, r = 1, n

        while l < r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l

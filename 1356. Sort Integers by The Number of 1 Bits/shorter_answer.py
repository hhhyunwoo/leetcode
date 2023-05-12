from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key= lambda x: (bin(x).count("1"), x))

solution = Solution()
print(solution.sortByBits([10,100,1000,10000]))
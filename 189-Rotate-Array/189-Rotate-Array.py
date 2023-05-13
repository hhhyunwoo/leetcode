from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            val = nums.pop()
            nums.insert(0, val)


solution = Solution()
print(solution.rotate([1,2,3,4,5,6,7], 3))
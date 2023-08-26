from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l >= 0 and r < len(nums) and l < r:
            mid = (l + r) // 2
            print(l,r,mid)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return l + 1

print(Solution().searchInsert([1,3,5,6],7))
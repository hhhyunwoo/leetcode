from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivotIdx = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                pivotIdx = i+1
                break
        normalNums = nums[pivotIdx:]+nums[:pivotIdx]
        print(normalNums)

        l, r = 0, len(normalNums)-1
        while l <= r:
            mid = (l+r)//2
            if normalNums[mid] == target:
                return (mid + pivotIdx) % len(nums)
            elif normalNums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1
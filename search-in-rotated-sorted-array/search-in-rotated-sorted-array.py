
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid -1
                else:
                    l = mid + 1

        return -1





# from typing import List
# 
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         pivotIdx = 0
#         for i in range(len(nums)-1):
#             if nums[i] > nums[i+1]:
#                 pivotIdx = i+1
#                 break
#         normalNums = nums[pivotIdx:]+nums[:pivotIdx]
#         print(normalNums)
# 
#         l, r = 0, len(normalNums)-1
#         while l <= r:
#             mid = (l+r)//2
#             if normalNums[mid] == target:
#                 return (mid + pivotIdx) % len(nums)
#             elif normalNums[mid] > target:
#                 r = mid - 1
#             else:
#                 l = mid + 1
# 
#         return -1
# 

sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0))
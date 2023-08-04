class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        flag = 1
        count = len(nums)
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                if flag >= 2:
                    nums[i] = 10001
                    count -= 1
                else:
                    flag += 1
            else:
                prev = nums[i]
                flag = 1
        nums.sort()
        nums = nums[:count]
        return len(nums)
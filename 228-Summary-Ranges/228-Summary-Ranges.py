from typing import List 

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i,j = 0,0
        for i in range(len(nums)):
            flag = 0
            if j > i: continue

            start, end = nums[i], nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == start + abs(j - i):
                    if j == len(nums) - 1:
                        end = nums[j]
                        flag = 1
                    continue
                else:
                    end = nums[j-1]
                    break
            if flag == 1:
                if start == end:
                    res = str(start)
                else:
                    res = str(start) + "->" + str(end)
                ans.append(res)
                break
            if start == end:
                res = str(start)
            else:
                res = str(start) + "->" + str(end)
            ans.append(res)
        return ans
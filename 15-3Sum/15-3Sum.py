from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums = sorted(nums)
        for i in range(0, len(nums)-2):
            s, e = i+1, len(nums)-1
            while s < e:
                summation = nums[i] + nums[s] + nums[e]
                if summation == 0:
                    ansTriplet = sorted([nums[i], nums[s], nums[e]])
                    if ansTriplet not in answer:
                        answer.append(ansTriplet)
                    s += 1
                elif summation <0:
                    s += 1
                else:
                    e -= 1
        return answer


solution = Solution()
print(solution.threeSum([-2,0,1,1,2]))
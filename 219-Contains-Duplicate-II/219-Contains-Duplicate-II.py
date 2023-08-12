class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numsDict = {}
        for i in range(len(nums)):
            if nums[i] in numsDict.keys():
                numsDict[nums[i]].append(i)
            else:
                numsDict[nums[i]] = [i]

        for _, v in numsDict.items():
            print(k,v)
            if len(v) >= 2:
                for i in range(0, len(v)-1):
                    print(v[i], v[i+1], abs(v[i] - v[i+1]),k)
                    if abs(v[i] - v[i+1]) <= k:
                        print(1)
                        return True
        return False
        
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = 1
        pos = 1
        for digit in digits[::-1]:
            val += digit * pos
            pos *= 10

        ans = []
        for c in str(val):
            ans.append(int(c))
        return ans

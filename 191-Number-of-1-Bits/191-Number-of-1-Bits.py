class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0 

        n = '{:032b}'.format(n)
        for i in range(32):
            if n[i] == "1":
                count += 1
        return count 
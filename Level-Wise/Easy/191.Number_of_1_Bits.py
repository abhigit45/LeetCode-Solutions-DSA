class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += (n&1)
            n >>= 1
        return count


        # res = 0
        # for i in range(32):
        #     if (n>>i) & 1:
        #         res += 1
        # return res
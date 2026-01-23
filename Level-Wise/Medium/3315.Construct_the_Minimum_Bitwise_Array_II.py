class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for n in nums:
            best = float('inf')

            for bit in range(31):
                if (n >> bit) & 1:
                    x = n ^ (1 << bit)
                    if (x | (x + 1)) == n:
                        best = min(best, x)

            if best == float('inf'):
                ans.append(-1)
            else:
                ans.append(best)

        return ans

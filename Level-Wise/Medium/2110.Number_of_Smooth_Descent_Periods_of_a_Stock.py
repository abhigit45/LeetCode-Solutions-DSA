class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = 0
        count = 1
        for i in range(1,len(prices)):
            if prices[i-1] - 1 == prices[i]:
                count += 1
                # res += count
            else:
                count = 1
                # res += count
            res += count
        return res + 1

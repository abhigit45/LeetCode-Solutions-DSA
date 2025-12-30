class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n(n+1)/2
        # 3(4)/2
        # 12/2
        # 6
        n = len(nums)
        total = int((n*n+n)/2)
        summ = 0
        for i in nums:
            summ += i
        return total - summ
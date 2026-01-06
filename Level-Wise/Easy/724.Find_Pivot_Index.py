class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # [1,8,11,17,22,28] Quamlavitve sum of num
        n = len(nums)
        cs = 0
        total = sum(nums)
        for i in range(0,len(nums)):
            val = total - cs - nums[i]
            if val == cs:
                return i
            cs += nums[i]
        return -1







        
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        cs = 0
        total = 0
        for num in nums:
            total += num
        for i in range(len(nums)):
            rs = total - cs - nums[i]
            if rs == cs:
                return i
            cs += nums[i]
        return -1

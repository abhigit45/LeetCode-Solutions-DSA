class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                total = nums[i] - nums[j]
                if abs(total) == k:
                    count += 1
        return count
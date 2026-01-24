class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        right = len(nums) - 1
        pair = []
        for left in range(len(nums)//2):
            pair.append(nums[left]+nums[right])
            right -= 1
        return max(pair)

        
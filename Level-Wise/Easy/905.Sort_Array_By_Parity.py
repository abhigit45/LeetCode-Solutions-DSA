class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[start] % 2 == 1:
                nums[start],nums[end] = nums[end],nums[start]
                end -= 1
            else:
                start += 1
        return nums

        
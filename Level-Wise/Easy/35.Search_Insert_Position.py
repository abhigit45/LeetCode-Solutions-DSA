class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        #binary search
        # left = 0
        # right = len(nums) -1
        # while left <= right:
        #     mid = (left+right)//2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return left
        # for i in range(len(nums)):
        #     if nums[i] >= target:
        #         return i
        # return len(nums)






        # while left <= right:
        #     # mid = (left+right) // 2
        #     if nums[right] < target:
        #         return right+1
        #     elif nums
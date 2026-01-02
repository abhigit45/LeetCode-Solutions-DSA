class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right]:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
            


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        for num in nums:
            if num != 0:
                nums[i],nums[j] = num,nums[i]
                i += 1
            j+=1

                
                






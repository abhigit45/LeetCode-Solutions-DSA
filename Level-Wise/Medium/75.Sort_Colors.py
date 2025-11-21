class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        med = 0
        high = len(nums) - 1
        while med<=high:
            if nums[med] == 0:
                nums[med],nums[low] = nums[low],nums[med]
                low +=1
                med +=1
            elif nums[med] == 1:
                med += 1
            else:
                nums[med],nums[high] = nums[high] ,nums[med]
                
                high -= 1

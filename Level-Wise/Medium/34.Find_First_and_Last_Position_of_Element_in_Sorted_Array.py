class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_pos = self.binarySearchLeft(nums,target)
        right_pos = self.binarySearchRight(nums,target)
        return [left_pos,right_pos]
        


    def binarySearchLeft(self,nums,target):
        n = len(nums)
        left = 0
        right = n -1
        left_most = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left_most = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left_most
    def binarySearchRight(self,nums,target):
        n = len(nums)
        left = 0
        right = n -1
        right_most = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right_most = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return right_most
                

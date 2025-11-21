class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isInc = False
        isDec = False
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                isInc = True
                
            if nums[i-1] > nums[i]:
                isDec = True
            if isInc and isDec:
                return False
        return True
        
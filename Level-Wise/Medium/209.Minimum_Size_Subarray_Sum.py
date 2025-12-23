class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currentSum = 0
        minWindow = float('inf')
        n = len(nums)
        left,right = 0 , 0
        while right< n:
            currentSum += nums[right]
            right += 1
            while currentSum >= target:
                curr_win_size = right - left
                if minWindow > curr_win_size :
                    minWindow = curr_win_size
                currentSum -=nums[left]
                left += 1
        if minWindow == float('inf'):
            return 0
        else:
            return minWindow
            


        
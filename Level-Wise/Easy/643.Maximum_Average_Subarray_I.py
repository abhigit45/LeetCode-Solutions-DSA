class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = 0
        left = 0
        for i in range(k):
            summ +=nums[i]
        max_sum = summ

        for i in range(k,len(nums)):
            summ -= nums[left]
            left += 1
            summ += nums[i]
            if summ > max_sum:
                max_sum = summ
        
        return max_sum/ k
            
        
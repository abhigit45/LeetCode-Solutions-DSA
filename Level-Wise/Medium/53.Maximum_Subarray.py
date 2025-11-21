class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0 
        for start in range(len(nums)):
            array_total = 0
            
            for j in range(start,len(nums)):
                # subarray = nums[start:j+1] #creating subarray
                array_total += nums[j] #without creating subarray direct padding value and compareing after the one array
                if array_total > total:
                    total = array_total
        return total

        
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        freq[0] = 1
        currSum = 0
        totalNum = 0
        n = len(nums)
        for i in range(n):
            currSum += nums[i]
            temp = currSum - k
            if temp in freq:
                totalNum += freq[temp]   
            if currSum in freq:
                freq[currSum] += 1
            else:
                freq[currSum] = 1

        return totalNum
            

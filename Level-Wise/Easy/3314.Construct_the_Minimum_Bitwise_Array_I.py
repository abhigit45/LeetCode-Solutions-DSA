class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            found = False
            for x in range(nums[i]):
                if x | (x + 1) == nums[i]:
                    found = True
                    res.append(x)
                    break
            if not found:
                res.append(-1)
        return res
            
        
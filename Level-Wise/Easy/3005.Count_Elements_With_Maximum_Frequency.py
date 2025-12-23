class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mapp = {}
        for i in nums:
            if not i in mapp:
                mapp[i] = 1
            else:
                mapp[i] += 1
        curr_max = 0
        count = 0
        for i in mapp:
            val = mapp[i]
            if curr_max < val:
                curr_max = val
                count = curr_max
            elif curr_max == val:
                count += val
        return count




            


    
        


        
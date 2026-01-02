class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # set
        seen = set()
        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)




        # #using HashMap
        # freq = {}
        # for num in nums:
        #     if not num in freq:
        #         freq[num] = 1
        #     else:
        #         freq[num] += 1
        # for val,count in freq.items():
        #     if count > 1:
        #         return val

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        freq = {}
        res = []
        for num in nums:
            unique_nums = set(num)
            for n in unique_nums:
                if not n in freq:
                    freq[n] = 1
                else:
                    freq[n] += 1
        for i,n in freq.items():
            if n == len(nums):
                res.append(i)
        return sorted(res)

        
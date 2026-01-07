class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            if not num in freq:
                freq[num] = 1
            else:
                return True
        return False
        
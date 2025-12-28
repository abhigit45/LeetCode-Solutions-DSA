class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapp = {}
        res = False
        for i in range(len(nums)):
            if not nums[i] in mapp:
                mapp[nums[i]] = i
            else:
                if abs(mapp[nums[i]] - i) <= k:
                    res =  True
                else:
                    mapp[nums[i]] = i
        return res
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = nums.copy()
        arr.sort()

        mapp = {}
        res = []
        for i in range(len(arr)):
            if arr[i] not in mapp:
                mapp[arr[i]] = i
        for num in nums:
            if num in mapp:
                res.append(mapp[num])
        return res

      
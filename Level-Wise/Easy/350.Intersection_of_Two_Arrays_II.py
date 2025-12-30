class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapp = {}
        res = []
        for num in nums1:
            if not num in mapp:
                mapp[num] = 1
            else:
                mapp[num] += 1
        for num in nums2:
            if num in mapp and mapp[num] > 0:
                res.append(num)
                mapp[num] -= 1
        return res
                
        
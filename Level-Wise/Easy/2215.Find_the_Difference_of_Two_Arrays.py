class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        nums1_res = []
        nums2_res = []
        for num in nums1:
            if not num in nums2_set and num not in nums1_res:
                nums1_res.append(num)
        for num in nums2:
            if not num in nums1_set and num not in nums2_res:
                nums2_res.append(num)
        return [nums1_res] + [nums2_res]



        
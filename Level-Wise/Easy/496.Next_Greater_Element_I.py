class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Monotonic Stack
        next_grt = {}
        stack = []
        for x in reversed(nums2):
            while stack and x >= stack[-1]:
                stack.pop()
            if stack:
                next_grt[x] = stack[-1]
            else:
                next_grt[x] = -1
            stack.append(x)
        res = []
        for x in nums1:
            res.append(next_grt[x])
        return res



        
        # # brute force
        # res = []
        # for target in nums1:
        #     target_found =  False
        #     next_grt = - 1
        #     for num in nums2:
        #         if num == target:
        #             target_found = True
        #         elif target_found and num > target:
        #             next_grt = num
        #             break
        #     res.append(next_grt)
        # return res
        
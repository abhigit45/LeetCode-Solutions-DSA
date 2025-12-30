class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # using TwoPointer
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if not res or res[-1] != nums1[i]:
                    res.append(nums1[i])
                j += 1
                i += 1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        return res
            


        # using hashmap
        # mapp = {}
        # res = []
        # for num in nums1:
        #     if not num in mapp:
        #         mapp[num] = True

        # for num in nums2:
        #     if num in mapp and mapp[num] == True:
        #         res.append(num)
        #         mapp[num] = False
        # return res

        
        



  

            


        
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #Approach1- optimal - binary Seach
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right)//2
            isEven = None
            if (right-mid)%2 == 0:
                isEven = True
            else:
                isEven = False

            ##Check right element(mid+1)
            if nums[mid] == nums[mid+1]:
                if isEven:
                    left = mid + 2 ##Becaure searching will start from mid + 1
                else:
                    right = mid - 1

            else: #nums[mid] != nums[mid+1]:   ##eg.[.,.,a,a(this is mid),b,b,c]
                if isEven:
                    right = mid
                else:
                    left = mid + 1 #becaure mid and and prev mid are already paired
        return nums[left]



        




        # Approach 1:
        # for i in range(0,len(nums)-1,2):
        #     if nums[i] != nums[i+1]:
        #         return nums[i]
        # return nums[-1] 

        
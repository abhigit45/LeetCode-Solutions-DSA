class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odds = []
        evens = []
        for num in nums:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
        res = []
        for i in range(len(evens)):
            res.append(evens[i])
            res.append(odds[i])

        return res


            
            

        



        # #In Place
        # even_idx = 0
        # odd_idx = 1
        # n = len(nums)

        # while even_idx < n and odd_idx < n:
        #     if nums[even_idx] % 2 == 0:
        #         even_idx += 2
        #     elif nums[odd_idx] % 2 == 1:
        #         odd_idx += 2
        #     else:
        #         nums[even_idx],nums[odd_idx] = nums[odd_idx],nums[even_idx]
        #         even_idx += 2
        #         odd_idx += 2
        # return nums


        
        


        
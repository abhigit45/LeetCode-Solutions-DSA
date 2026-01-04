class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            curr = []
            count = 0
            for i in range(1,int(sqrt(num)+1)):
                if num % i == 0:
                    other = num//i
                    if i == other:
                        curr.append(i)
                        count += i
                    else:
                        curr.append(i)
                        curr.append(other)
                        count += i
                        count += other
                    if len(curr) > 4:
                        break
            if len(curr) == 4:
                res += count
        return res

            






        # bruteForce
        # res = 0
        # res_arr = []
        # for num in nums:
        #     level_arr = []
        #     count = 0

        #     for i in range(1,sqrt(num+1)):
        #         other = 

        #         if num % i == 0:
        #             level_arr.append(i)
                    
        #             count += i
        #     if len(level_arr) >= 4:
        #         res += count
        # return res

        
        
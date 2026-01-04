from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = [0] * 10
        for d in digits:
            freq[d] +=1
        res = []

        for i in range(1,10):
            for j in range(10):
                for k in range(0,10,2):
                    if freq[i] > 0 and freq[j] > 0 and freq[k] > 0:
                        freq[i] -= 1
                        freq[j] -= 1
                        freq[k] -= 1
                        if freq[i] >=0 and freq[j] >= 0 and freq[k] >= 0:
                            res.append(i*100+j*10+k)
                        freq[i] += 1
                        freq[j] += 1
                        freq[k] += 1
        return res
                        


 


        # # BRUTEFORCE
        # res = set()
        # for i in range(len(digits)):
        #     for j in range(len(digits)):
        #         for k in range(len(digits)):
        #             if i != j and j != k and i != k and digits[k]%2==0:
        #                 num = digits[i] * 100 + digits[j] * 10 + digits[k]
        #                 if digits[i] != 0:
        #                     res.add(num)
        # return sorted(res)
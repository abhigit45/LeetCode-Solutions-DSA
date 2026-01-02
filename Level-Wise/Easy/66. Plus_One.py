class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(1,len(digits)+1):
            if digits[-i] < 9:
                digits[-i] += 1
                return digits

            elif digits[-i] == 9:
                digits[-i] = 0
               
            
        # digits.insert(0,1)
        digits[:0] = [1]

        return digits



        
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(-1,-len(digits)-1,-1):
            if digits[i] < 9:
                digits[i] = digits[i] + 1
                return digits
            elif digits[i] == 9:
                digits[i] = 0
        digits.insert(0,1)
        return digits







        # dig_str = ""
        # for dig in digits:
        #     dig_str += str(dig)
        # res = int(dig_str) + 1
        # res_str = str(res)
        # output = []
        # for i in res_str:
        #     output.append(int(i))
        # return output




                
                

        
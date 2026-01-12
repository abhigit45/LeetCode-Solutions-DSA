class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        total = 1
        if num == 1:
            return False
        for i in range(2,int(sqrt(num)+1)):
            if num % i == 0:
                total += i
                if i!=num//i:
                    total += num //i
        # total = total - num
        if total == num:
            return True
        else:
            return False
        

        
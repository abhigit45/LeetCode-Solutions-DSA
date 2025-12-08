class Solution:
    def countTriples(self, n: int) -> int:
        c_square = set()
        for i in range(1, n+1):
            c_square.add(i*i)
        count = 0
        for a in range(1,n+1):
            for b in range(1, n+1):
                summ = a*a + b*b
                if summ in c_square:
                    count += 1
        return count
                
        
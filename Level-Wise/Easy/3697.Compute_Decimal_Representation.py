class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        res = []
        n_str = str(n)
        length =len(n_str)
        for i,ch in enumerate(n_str):
            # int(i)
            digit = int(ch)
            power = length - i - 1
            if digit != 0:
                
            
                res.append(digit *  (10 ** power))
        return res
            
            
        
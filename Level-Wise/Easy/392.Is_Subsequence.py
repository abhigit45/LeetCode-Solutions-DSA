class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True  
        
        ptr = 0
        m = len(s)
        
        for char in t:
            if ptr < m and char == s[ptr]:
                ptr += 1
            if ptr == m:
                return True
        
        return False

        #hardcode
        # n = len(t)
        # res = False
        # ptr =  0
        # m = len(s) - 1
        # for i in range(n):
        #     if t[i] == s[ptr]:
        #         if m == ptr:
        #             res = True
        #         ptr += 1
        # return res
                


        
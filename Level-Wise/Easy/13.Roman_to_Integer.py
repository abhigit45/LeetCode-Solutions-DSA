class Solution:
    def romanToInt(self, s: str) -> int:
        mapp = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        number = 0
        for i in range(1,len(s)+1):
            if s[-i] == 'I' and s[-i+1] == 'V' or s[-i] == 'I' and s[-i+1] == 'X':
                number -= 1
            elif s[-i] == 'X' and s[-i+1] == 'L' or s[-i] == 'X' and s[-i+1] == 'C':
                number -= 10
            elif s[-i] == 'C' and s[-i+1] == 'D' or s[-i] == 'C' and s[-i+1] == 'M':
                number -= 100
            else:
                number += mapp[s[-i]]
        return number
    
    
    

##more cleaner version
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         mapp = {
#             'I': 1, 'V': 5, 'X': 10,
#             'L': 50, 'C': 100,
#             'D': 500, 'M': 1000
#         }

#         total = 0
#         prev_value = 0

#         for char in reversed(s):
#             curr_value = mapp[char]
#             if curr_value < prev_value:
#                 total -= curr_value
#             else:
#                 total += curr_value
#             prev_value = curr_value

#         return total


        
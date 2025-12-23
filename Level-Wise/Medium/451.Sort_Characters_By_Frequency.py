class Solution:
    def frequencySort(self, s: str) -> str:
        freq_map = {}
        for i in s:
            if not i in freq_map:
                freq_map[i] = 1
            else:
                freq_map[i] += 1
        tuple_list = list(freq_map.items())
        n = len(tuple_list)
        for i in range(n):
            for j in range(0,n - i -1):
                left = tuple_list[j][1]
                right = tuple_list[j+1][1]
                if left < right:
                    tuple_list[j],tuple_list[j+1] = tuple_list[j+1],tuple_list[j]
        res = ""
        for char,freq in tuple_list:
            res += char*freq
        return res

        





        
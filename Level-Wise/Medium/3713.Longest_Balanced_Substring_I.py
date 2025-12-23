class Solution:
    def longestBalanced(self, s: str) -> int:
        max_len = 0
        n = len(s)
        for start in range(n):
            freq = {}
            for end in range(start,n):
                char = s[end]
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1

                values = list(freq.values())
                if min(values) == max(values):
                    curr_len = end - start +1 
                    max_len = max(max_len,curr_len)
        return  max_len
        
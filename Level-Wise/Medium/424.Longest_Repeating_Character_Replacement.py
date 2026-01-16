class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        max_freq = 0
        maxWindow = 0
        left = 0
        for right in range(len(s)):
            freq[ord(s[right]) - ord('A')] += 1

            max_freq = max(max_freq,freq[ord(s[right]) - ord('A')])

            while (right - left + 1)  - max_freq > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1
                
            # windowLen = right - left + 1
            # if windowLen - max_freq  > k:
            #     freq[ord(s[left]) - ord('A')] -= 1
            #     left += 1
            # windowLen = right - left + 1
            maxWindow = max(maxWindow,right - left + 1)

        return maxWindow
            
            







        
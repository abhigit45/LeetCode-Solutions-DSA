class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        track_s = set()
        for right in range(len(s)):
            while s[right] in track_s:
                track_s.remove(s[left])
                left +=1

            track_s.add(s[right])
            max_len = max(max_len, right - left +1)
        return max_len
            


            
        
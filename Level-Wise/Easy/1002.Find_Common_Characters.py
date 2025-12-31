class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = [0]*26
        for ch in words[0]:
            freq[ord(ch) - ord('a')] += 1

        for word in words[1:]:
            common = [0] * 26
            for ch in word:
                common[ord(ch) - ord('a')] += 1
            for i in range(26):
                freq[i] = min(freq[i],common[i])
        
        res = []
        for i in range(len(freq)):
            val = i + ord('a')
            for j in range(freq[i]):
                
                res.append(chr(val))
        return res


        
        return freq
            
        
            
        

      
        
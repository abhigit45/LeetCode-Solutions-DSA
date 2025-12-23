class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_freq = {}
        word2_freq = {}
        if len(word1) != len(word2):
            return False
        if set(word1) == set(word2):
            for i in range(len(word1)):
                if word1[i] in word1_freq:
                    word1_freq[word1[i]] += 1
                else:
                    word1_freq[word1[i]] = 1
                if word2[i] in word2_freq:
                    word2_freq[word2[i]] += 1
                else:
                    word2_freq[word2[i]] = 1
        else:
            return False
        
        
        if sorted(word1_freq.values()) == sorted(word2_freq.values()):
            return True
        else:
            return False
        
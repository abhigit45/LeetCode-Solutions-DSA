class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        mapp = {}
        for char in chars:
            if not char in mapp:
                mapp[char] = 1
            else:
                mapp[char] += 1
        for word in words:
            n = len(word)
            mapp1 = mapp.copy()
            i = 0
            count = 0
            while i < n:
                if word[i] in mapp1 and mapp1[word[i]] > 0:
                    mapp1[word[i]] -= 1
                    count += 1
                    i += 1
                else:
                    count = 0
                    break
            res += count
        return res
            

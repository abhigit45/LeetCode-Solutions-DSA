class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mapp = {}
        for i in range(len(magazine)):
            if not magazine[i] in mapp:
                mapp[magazine[i]] = 1
            else:
                mapp[magazine[i]] += 1
        for i in ransomNote:
            if i in mapp and mapp[i]>0:
                mapp[i] -= 1
            else:
                return False
        return True
        
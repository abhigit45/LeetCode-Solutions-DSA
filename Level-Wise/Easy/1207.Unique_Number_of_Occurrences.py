class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        n = len(arr)
        for i in range(n):
            if arr[i] in freq:
                freq[arr[i]] += 1
            else:
                freq[arr[i]] = 1
        check_rep = set(freq.values())
        if len(freq.values()) == len(check_rep):
            return True
        else:
            return False
    
        
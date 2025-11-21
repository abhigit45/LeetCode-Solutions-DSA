class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
    
        total = 0
        n = len(arr)
        for start in range(n):
            current_sum = 0
            for end in range(start,n):
                current_sum += arr[end]
                length = end - start +1
                if length % 2 == 1:
                    total += current_sum
        return total
        

        
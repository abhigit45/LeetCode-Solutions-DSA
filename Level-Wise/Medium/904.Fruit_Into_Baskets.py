class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = {}
        left = 0
        max_num = 0
        for right in range(len(fruits)):
            if fruits[right] in freq:
                freq[fruits[right]] += 1
            else:
                freq[fruits[right]] = 1

            while len(freq) > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    freq.pop(fruits[left])
                left += 1
                
            max_num = max(max_num,right -left + 1)
        return max_num
            

            
 
            

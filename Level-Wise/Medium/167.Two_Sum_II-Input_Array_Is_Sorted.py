class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        res = []
        while start < end:
            curr_sum = numbers[start] + numbers[end]
            if curr_sum == target:
                res.append(start+1)
                res.append(end+1)
                return res
            elif curr_sum> target:
                end -= 1
            else:
                start += 1
        return res
        
            
        
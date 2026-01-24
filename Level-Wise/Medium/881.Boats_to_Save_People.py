class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        right = len(people) - 1
        left = 0
        count = 0
        while left <= right:
            pair = people[left] + people[right]
            if pair <= limit:
                count += 1
                left += 1
                right -= 1
            else:
                count += 1
                right -= 1
            
        return count




        
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apple = sum(apple)
        capacity.sort()
        count = 0
        cap_sum = 0
        for cap in reversed(capacity):
            if cap_sum < total_apple:
                count += 1
                cap_sum += cap
           
        return count

            

      
# class Solution:
#     def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
#         total_apple = sum(apple)
#         capacity.sort()
#         count = 0
#         cap_sum = 0

#         for cap in reversed(capacity):
#             if cap_sum >= total_apple:
#                 break
#             cap_sum += cap
#             count += 1

#         return count

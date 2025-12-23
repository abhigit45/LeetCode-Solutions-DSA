# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        curr = head
        length = 0
        lst = []
        while curr:
            lst.append(curr.val)
            curr = curr.next
            length += 1

        res = [0] * len(lst)
        stack = []
        for i in range(len(lst)):
            if not stack:
                stack.append(i)
            else:
                while stack and lst[i] > lst[stack[-1]]:
                    res[stack[-1]] = lst[i]
                    stack.pop()
            stack.append(i)
        return res
            

        
            


        
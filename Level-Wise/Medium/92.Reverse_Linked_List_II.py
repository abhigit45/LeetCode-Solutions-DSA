# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        for _ in range(left-1):
            prev = curr
            curr = curr.next
        for _ in range(right - left):
            temp = prev.next
            node_to_move = curr.next      #3                #4
            prev.next = node_to_move      #1->3             #1-> 4
            curr.next = node_to_move.next #2 -> 4           # 2-> 5
            node_to_move.next = temp      #3 -> 2           # 4 -> 3
            # prev = prev.next
            # 0 1 2 3 4 5
            # 0 1 3 2 4 5 iteration one
            # 0 1 4 3 2 5 iteration two
            

        return dummy.next
           
            
        
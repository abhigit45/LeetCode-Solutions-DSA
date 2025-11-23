# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        length = 0
        while curr:
            curr = curr.next
            length += 1
        curr = head
       
        while length >= k:

            for _ in range(k-1):
                next_head_of_group = prev.next
                node_to_move = curr.next #2
                curr.next = node_to_move.next  #1->3
                prev.next = node_to_move #0->2
                node_to_move.next = next_head_of_group#2->1
            prev = curr
            curr = curr.next
            length -= k

            
        return dummy.next


                

        
        
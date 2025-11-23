# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        dummy2.next = head
        prev = dummy2
        current_dumm = dummy1
        current = head
        
        while current :
            if current.val >= x:
                current_dumm.next = current
                prev.next = current.next
                current_dumm = current_dumm.next

            else:
                prev = prev.next
            current =current.next
  
        prev.next = dummy1.next
        current_dumm.next = None
        return dummy2.next
            


        
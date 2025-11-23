# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy_tail = dummy
        current = head.next
        value = 0
        while current:
            
            if current.val != 0:
                value += current.val
            else:
                dummy_tail.next = ListNode(value)
                dummy_tail = dummy_tail.next
                value = 0
            current = current.next
        dummy_tail.next = None
        return dummy.next
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        que1 = deque()
        que2 = deque()
        que1.append(p)
        que2.append(q)
        
        while que1 and que2:
            node1 = que1.popleft()
            node2 = que2.popleft()

            if not node1 and not node2:
                continue

            if not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False
            que1.append(node1.left)
            que1.append(node1.right)
            que2.append(node2.left)
            que2.append(node2.right)
        return True
            
            
        

                
                





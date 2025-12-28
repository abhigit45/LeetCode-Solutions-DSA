# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        que = deque()
        que.append(root)
        res = []
        if root == None:
            return False
        
        while que:
            n = len(que)
            prev = None 
            level = []
            
            for i in range(n):
                node = que.popleft()
                level.append(node.val)

                if len(res) % 2 == 0:
                    if node.val % 2 == 1:
                        if prev is not None: 
                            if prev >= node.val:
                                return False
                       
                        prev = node.val
                    else:
                        return False
                else:
                    if node.val % 2 == 0:
                        if prev is not None: 
                            if prev <= node.val:
                                return False
                        
                        prev = node.val
                    else:
                        return False

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                
            res.append(level)
        return True

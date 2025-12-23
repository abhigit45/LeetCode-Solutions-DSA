"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        count = 0
        que = deque()
        que.append(root)
        if root is None:
            return 0
        while que:
            n = len(que)
            for i in range(n):
                node = que.popleft()
                if node.children:
                    for child in node.children:
                        que.append(child)
       
            count += 1
                    
        return count
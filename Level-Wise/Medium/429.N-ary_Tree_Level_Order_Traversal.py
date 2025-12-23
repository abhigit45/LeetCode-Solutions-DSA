"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        que = deque()
        res = []
        que.append(root)
        if not root:
            return []
        while que:
            n = len(que)
            level = []
            for i in range(n):
                node = que.popleft()
                level.append(node.val)
                if node.children:
                    for children in node.children:
                        que.append(children)
            res.append(level)
        return res
        
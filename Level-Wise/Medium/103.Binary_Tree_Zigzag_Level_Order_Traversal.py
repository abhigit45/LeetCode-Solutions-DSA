# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = deque()
        res = []
        que.append(root)
        if root == None:
            return []
        while que:
            n = len(que)
            level = []
            for i in range(n):
                node = que.popleft()
                level.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            if len(res) % 2 != 0 :
                res.append(level[::-1])
            else:
                res.append(level)
        return res
        
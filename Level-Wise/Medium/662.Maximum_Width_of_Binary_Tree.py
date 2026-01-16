# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        que = deque([(root,0)])
        res = 0
        if not root:
            return 0
        while que:
            n = len(que)
            _,first_index = que[0]
            _,last_index = que[-1]
            res = max(res,last_index - first_index+1)
            for i in range(n):
                node,index = que.popleft()
                if node.left:
                    que.append([node.left,2*index])
                if node.right:
                    que.append([node.right, 2*index+1])
        return res

       
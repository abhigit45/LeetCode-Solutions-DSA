# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        path = []
        sumPath = []
        path.append(root)
        sumPath.append(root.val)
        while path:
            temp = path.pop()
            tempVal = sumPath.pop()
            if temp.left == None and temp.right == None and tempVal == targetSum:
                return True
            if temp.right != None:
                path.append(temp.right)
                sumPath.append(temp.right.val + tempVal)

            if temp.left != None:
                path.append(temp.left)
                sumPath.append(temp.left.val + tempVal)
        return False
        
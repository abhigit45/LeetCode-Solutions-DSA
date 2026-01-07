# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def totalSum(self,root):
        if not root:
            return 0
        leftSubTreeSum = self.totalSum(root.left)
        rightSubTreeSum = self.totalSum(root.right)
        summ = root.val +leftSubTreeSum + rightSubTreeSum

        return summ

    
    def find(self,root):
        if not root:
            return 0
        leftSum = self.find(root.left)
        RightSum = self.find(root.right)
        subTreeSum = root.val + leftSum + RightSum
        remainingSubTreeSum = self.SUM - subTreeSum
        self.maxP = max(remainingSubTreeSum *subTreeSum,self.maxP )
        return subTreeSum

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.maxP = 0
        self.SUM = self.totalSum(root)
        self.find(root)
        return self.maxP % (10**9 + 7)

        
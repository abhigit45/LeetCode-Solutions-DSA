# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        res = []
        path = []
        total = 0
        def dfs(node,path,total):
            if node is None:
                return
            path.append(node.val)
            total += node.val

            if node.left is None and node.right is None and total == targetSum:
                res.append(path[:])
            if node.left != None:
                dfs(node.left,path,total)
            if node.right != None:
                dfs(node.right,path,total)
            path.pop()
        dfs(root,path,total)
        return res








        # result = []
        # path = []
        # total = 0

        # def dfs(node, path, total):
        #     if not node:
        #         return

        #     path.append(node.val)
        #     total += node.val

        #     if not node.left and not node.right and total == targetSum:
        #         result.append(path[:])  

        #     dfs(node.left, path, total)
        #     dfs(node.right, path, total)

        #     path.pop()  

        # dfs(root, path, total)
        # return result
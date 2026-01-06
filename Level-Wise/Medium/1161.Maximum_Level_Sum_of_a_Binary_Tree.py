# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que = deque([root])
        max_sum = float('-inf')
        max_level = 0
        level = 0
        while que:
            n = len(que)
            curr_sum = 0
            for i in range(n):
                node = que.popleft()
                curr_sum += node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            level += 1
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_level = level
        return max_level



        



        # if not root:
        #     return 0
        # que = deque([root])
        # max_sum = float('-inf')
        # max_level = 0
        # level = 0
        
        # while que:
        #     n = len(que)
            
        #     curr_sum = 0
        #     for i in range(n):
        #         node = que.popleft()
        #         curr_sum += node.val
        #         if node.left:
        #             que.append(node.left)
        #         if node.right:
        #             que.append(node.right)
        #     level += 1
        #     if curr_sum > max_sum:
        #         max_sum = curr_sum
        #         max_level = level
        # return max_level
            

        
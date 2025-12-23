# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        count = 1
        que = deque()
        que.append(root)
        

        while que:
            n = len(que)
            node = que.popleft()
            for i in range(n):
                if node.left == None and node.right == None:
                    return count 
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            count += 1
        return count
        
            
                
            

        
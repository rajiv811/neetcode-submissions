# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Steps
        1. Flatten BST (Lowest to largest)
        - Go all the way down left subtree
        - Then take right subtree values
        2. Return index k-1
        """
            
        res = []
        def dfs(root):
            if root.left:
                dfs(root.left)
            res.append(root.val)
            if root.right:
                dfs(root.right)
        dfs(root)
        print(res)
        return res[k-1]
            

        